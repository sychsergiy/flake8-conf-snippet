import nox

TARGETS = ["test.py", "anner"]


@nox.session(reuse_venv=True)
def dev(session):
    session.install("-r", "requirements-dev.txt")
    session.install("pre-commit")
    session.run("pre-commit", "install", "-t", "pre-commit")


@nox.session(reuse_venv=True)
def reformat(session):
    session.install("-r", "requirements-lint.txt")

    session.run("black", *TARGETS)
    session.run("isort", *TARGETS)


@nox.session(reuse_venv=True)
def lint(session):
    session.install("-r", "requirements-lint.txt")
    session.run("flake8", *TARGETS)
