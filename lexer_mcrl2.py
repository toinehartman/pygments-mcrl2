from pygments.lexer import RegexLexer, words
from pygments import token

from pygments.lexers.python import PythonLexer


class bounded_words(words):
    def __init__(self, words):
        super().__init__(words, suffix=r"\b")


builtin_types = ("Int", "Nat", "Bool")
builtin_actions = ("tau", "delta")
builtin_constants = ("true", "false")


class mCRL2(RegexLexer):
    name = "mCRL2"
    aliases = ["mcrl2"]
    filenames = ["*.mcrl2"]

    tokens = {
        "root": [
            (bounded_words(builtin_types), token.Keyword.Type),
            (bounded_words(("init", "act", "proc")), token.Keyword.Declaration),
            (bounded_words(("allow", "hide", "rename", "comm")), token.Name.Builtin),
            (bounded_words(("map", "eqn", "var")), token.Keyword.Declaration),
            (bounded_words(("sum", )), token.Name.Builtin),
            (r"[\.\+\-\*\/\!#=\<\>\[\]]", token.Operator),
            (bounded_words(builtin_actions), token.Name.Constant),
            (bounded_words(builtin_constants), token.Keyword.Constant),
            (r"\d+", token.Number.Integer),
            (r"%.*", token.Comment.Single),
            (r"[#,;:\(\)]", token.Punctuation),
            (r"\w[\w\d]*", token.Name),
            (r"\s+", token.Whitespace),
            (r".+", token.Text)
        ]
    }


class mCF(RegexLexer):
    name = "mCF"
    aliases = "mcf"
    filenames = ".mcf"

    tokens = {
        "root": [
            (bounded_words(builtin_types), token.Keyword.Type),
            (bounded_words(("mu", "nu")), token.Name.Builtin),
            (bounded_words(("sum", )), token.Name.Builtin),
            (bounded_words(("forall", "exists", )), token.Name.Builtin),
            (r"[\.\+\-\*\/\!#=\<\>\[\]]", token.Operator),
            (r"(\|\||\||&&)", token.Operator),
            (bounded_words(builtin_actions), token.Name.Constant),
            (bounded_words(builtin_constants), token.Keyword.Constant),
            (r"\d+", token.Number.Integer),
            (r"%.*", token.Comment.Single),
            (r"[#,;:\(\)]", token.Punctuation),
            (r"\w[\w\d]*", token.Name),
            (r"\s+", token.Whitespace),
            (r".+", token.Text)
        ]
    }
