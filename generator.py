from urllib.parse import quote_plus
from textwrap import dedent
projects = [
    {
        "repo": "gtalarico/pyairtable",
        "website": "",
        "rtd": "pyairtable",
        "name": "pyAirtable",
        "status": "🟢",
        "type": "Library",
    },
    {
        "repo": "aecworks/aec.works-web",
        "website": "https://aec.works",
        "rtd": "",
        "name": "aec.works",
        "status": "🟢",
        "type": "Website",
    },
    {
        "repo": "",
        "website": "https://apidocs.co",
        "rtd": "",
        "name": "ApiDocs.co",
        "status": "🟢",
        "type": "Website",
    },
    {
        "repo": "",
        "website": "https://www.revitapidocs.com",
        "rtd": "",
        "name": "Revit Api Docs",
        "status": "🟢",
        "type": "Website",
    },
    {
        "repo": "gtalarico/aec-startups",
        "website": "https://aecstartups.com",
        "rtd": "",
        "name": "AecStartups",
        "status": "🟢",
        "type": "Website",
    },
    {
        "repo": "gtalarico/flask-vuejs-template",
        "website": "",
        "rtd": "",
        "name": "Flask Vue JS Template",
        "status": "🟠",
        "type": "DevTool",
    },
    {
        "repo": "gtalarico/django-vue-template",
        "website": "",
        "rtd": "",
        "name": "Django Vue JS Template",
        "status": "🟠",
        "type": "DevTool",
    },
    {
        "repo": "gtalarico/ironpython-stubs",
        "website": "",
        "rtd": "",
        "name": "Iron Python Stubs",
        "status": "🟠",
        "type": "DevTool",
    },
    {
        "repo": "gtalarico/revitpythonwrapper",
        "website": "",
        "rtd": "revitpythonwrapper",
        "name": "Revit Python Wrapper",
        "status": "🟠",
        "type": "Library",
    },
    {
        "repo": "gtalarico/pm",
        "website": "",
        "rtd": "",
        "name": "pm",
        "status": "🔴",
        "type": "DevTool",
    },
    {
        "repo": "gtalarico/pipenv-pipes",
        "website": "",
        "rtd": "pipenv-pipes",
        "name": "pipes",
        "status": "🔴",
        "type": "DevTool",
    },
    {
        "repo": "gtalarico/pyrevitplus",
        "website": "",
        "rtd": "",
        "name": "PyRevitPlus",
        "status": "🔴",
        "type": "Library",
    },
    {
        "repo": "gtalarico/python-algorithms",
        "website": "",
        "rtd": "",
        "name": "Python Algorithms",
        "status": "⚪️",
        "type": "Learning",
    },
    {
        "repo": "",
        "website": "https://grid-solver.netlify.app",
        "rtd": "",
        "name": "Grid Solver",
        "status": "⚪️",
        "type": "Learning",
    },
    {
        "repo": "gtalarico/vue-threejs-rhino-demo",
        "website": "https://vue-threejs-rhino-viewer.netlify.app",
        "rtd": "",
        "name": "Vue 3JS Rhino",
        "status": "⚪️",
        "type": "Learning",
    },
    {
        "repo": "gtalarico/interactive-elastic-analyzer",
        "website": "https://interactive-elastic.herokuapp.com",
        "rtd": "",
        "name": "Elastic Search Analyser",
        "status": "⚪️",
        "type": "Learning",
    }
]

headings = ["Name", "Status", "Type", "Links"]
rows = []
for p in projects:

    repo, website, rtd, name, status, type = p["repo"], p["website"], p["rtd"], p["name"], p["status"], p["type"]

    url_encoded = "" if not website else quote_plus(website)
    row_tds = [
        f"<td>{name}</td>",
        f"<td>{status}</td>",
        f"<td>{type}</td>",
        "<td>\n\n",
        "" if not p["rtd"] else f"\n[![{name}](https://img.shields.io/readthedocs/{rtd}?style=flat-square)](https://{rtd}.readthedocs.io)",
        "" if not p["website"] else f"\n[![{name}](https://img.shields.io/website?style=flat-square&url={url_encoded})]({website})",
        "" if not p["repo"] else f"\n[![GitHub Repo stars](https://img.shields.io/github/stars/{repo}?style=flat-square)](https://github.com/{repo})",
        "\n\n</td>"
    ]

    rows.append("".join(row_tds).format(**p))

heading_tds = "".join([f"<th>{name}</th>" for name in headings])
rows_tds = "".join([f"<tr>{name}</tr>\n" for name in rows])
html = f"""
<table>
 <tr>
  {heading_tds}
 </tr>
{rows_tds}
</table>
"""

print(dedent(html))
