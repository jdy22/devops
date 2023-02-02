import subprocess
from flask import Blueprint, request, render_template, abort, send_file
from literature_searcher import query_processor
from tempfile import TemporaryDirectory
from pathlib import Path


file_name = {"MARKDOWN": "result.md", "PDF": "result.pdf"}
mimetype = {"MARKDOWN": "text/markdown", "PDF": "application/pdf"}

bp = Blueprint("literature_searcher", __name__)


@bp.route("/")
def index():
    return render_template("search_page.html")


# # COMMENT-OUT FOR STAGE 3 ------------------------------------
# @bp.route("/search_results", methods=["GET", "POST"])
# def process_query():
#     if query := request.form["search_query"]:
#         search_results = query_processor.process(query)
#         return render_template("search_results.html", search_results=search_results)
#     abort(400, "You did not enter a query")


# ------------------------------------------------------------


# UNCOMMENT FOR STAGE 3 --------------------------------------
@bp.route("/search_results", methods=["GET", "POST"])
def process_query():
    if query := request.form["search_query"]:
        search_results = query_processor.process(query)
        response_type = request.form["response_type"]
        if response_type == "HTML":
            return render_template("search_results.html", search_results=search_results)

        # response_type is either MARKDOWN or PDF
        with TemporaryDirectory() as tmp:

            # We need the markdown regardless
            md_file_path = create_markdown_file(
                content=formatted_response(query, search_results),
                file_path=tmp / Path("temp.md"),
            )

            response_file_path = md_file_path
            if response_type == "PDF":
                response_file_path = create_pdf_from_markdown(
                    md_file_path=md_file_path, pdf_file_path=tmp / Path("temp.pdf")
                )

            return send_file(
                response_file_path,
                mimetype=mimetype[response_type],
                download_name=file_name[response_type],
                as_attachment=True,
            )
    abort(400, "You did not enter a query")
# ------------------------------------------------------------


def formatted_response(query: str, results: [str]) -> str:
    compound_results = "\n\n --- \n\n".join(results)
    return f"## Query: {query}\n\n{compound_results}"


def create_markdown_file(content: str, file_path: Path) -> Path:
    with open(file_path, "w") as md_file:
        md_file.write(content)
    return file_path


def create_pdf_from_markdown(md_file_path: Path, pdf_file_path: Path) -> Path:
    # Use pandoc to convert markdown to PDF.
    # In a real-world scenario we'd have some good error handling here.
    with open(pdf_file_path, "w"):
        pandoc_invocation = f"pandoc -o {pdf_file_path} {md_file_path}"
        subprocess.run(pandoc_invocation.split(" "))
    return pdf_file_path
