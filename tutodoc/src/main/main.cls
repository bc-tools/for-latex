% == \CLS OPTIONS == %

%%%
% refs::
%     + https://tex.stackexchange.com/a/729929/6880
%     + https://tex.stackexchange.com/a/729913/6880
%%%

\ExplSyntaxOn

\msg_set:nnnn { tutodoc ~ (main) }
  { main : scrartcl-illegal-option }
  { The ~ option ~ << ~ #1 ~ >> ~ is ~ not ~ allowed. }
  { \msg_see_documentation_text:n { tutodoc } }


\newcommand{\tutodoc@theme}{color}


%%%
% prototype::
%     theme    : the theme to format the document.
%     fontsize : this key is one of those of the '''scrartcl'' class.
%                As \tutodoc imposes the value of this key, we must
%                forbid its use.
%     DIV      : similar to the preceding key but here we just want
%                to avoid any use of special ''DIV'' value.
%%%
\keys_define:nn { tutodoc / main / class / options } {
  theme .choices:nn = {
    bw,
    color,
    dark,
    draft
  } {
    \exp_args:NNV \renewcommand \tutodoc@theme \l_keys_choice_tl
  },
  fontsize .code:n = {
    \msg_error:nnn { tutodoc ~ (main) }
      { main : scrartcl-illegal-option }
      { fontsize }
  },
  DIV .code:n = {
    \msg_error:nnn { tutodoc ~ (main) }
      { main : scrartcl-illegal-option }
      { DIV }
  },
}

\PassOptionsToClass{ fontsize = 10pt }{ scrartcl }

\DeclareUnknownKeyHandler[ tutodoc / main / class / options ]{
  \PassOptionsToClass{ \CurrentOption }{ scrartcl }
}

\ProcessKeyOptions[ tutodoc / main / class / options ]

\LoadClass{ scrartcl }

\ExplSyntaxOff


% == OPTIONS FOR PACKAGES IMPORTED BY OTHER ONES == %

% xcolor is loaded by minted and tcolorbox.
\PassOptionsToPackage{svgnames}{xcolor}


% == IMPORTS == %

\RequirePackage{geometry}

\RequirePackage{marginnote}
\RequirePackage{fontawesome5}
\RequirePackage{keytheorems}

\RequirePackage{clrstrip}

% Special settings for minted need to be done before the loading of
% the tcolorbox library minted.
\RequirePackage[highlightmode = immediate]
               {minted}

\RequirePackage{tcolorbox}
\tcbuselibrary{
  minted,
  breakable,
  skins
}

\RequirePackage{hyperref}


%%%
% We delegate the management of quoting to the ''csquotes'' package,
% which takes care of the locale settings.
%
% warning::
%     We must load ''inputenc'' before ''csquotes''
%%%
\RequirePackage[utf8]
               {inputenc}

\RequirePackage{csquotes}


% == LOCALE SETTINGS == %

\ExplSyntaxOn

\msg_set:nnnn { tutodoc ~ (main) }
  { main : unsupported-lang }
  {
    unsupported ~ language ~ << ~ #1 ~ >>. %
    ~ %
    We ~ will ~ use ~ << ~ en ~ >>.
  }
  { \msg_see_documentation_text:n { tutodoc } }


% Management of English composition rules.
\newcommand{\tutodoc@use@english}{\relax}

% Babel requires colon management for our translations.
\newcommand{\tutodoc@colon}{:}

\AtBeginDocument{
% Babel is used.
  \@ifpackageloaded{babel}{
% We must take care of colons and spacing.
    \iflanguage{french}{
      \renewcommand{\tutodoc@colon}{\babelshorthand{:}}
    }{}
  }{}

% Polyglossia is used.
  \@ifpackageloaded{polyglossia}{
% If polyglossia is used, we must load english if necessary
% (see the ''\tutodoc@use@english'' macro below).
    \iflanguageloaded{english}{}{
      \setotherlanguage{english}
    }
  }{}%

  \newcommand{\tdoclang}{\BCPdata{language}}

% We must take care of English rules for English contents.
  \renewcommand\tutodoc@use@english{%
    \foreignlanguage{english}%
  }

% If the lang is not supported, we emit a warning and just turn
% to the english language.
  \makeatletter

  \InputIfFileExists{../main/tutodoc-main-locale-\tdoclang.cfg.cls.sty}{}{
    \input{../main/tutodoc-main-locale-en.cfg.cls.sty}

    \msg_critical:nnx { tutodoc ~ (main) }
      { main : unsupported-lang }
      { \tdoclang }
  }

  \makeatother
}

\ExplSyntaxOff


% == GEOMETRY SETTINGS == %

\geometry{
  top            = 1.9cm,
  bottom         = 1.9cm,
  left           = 2.25cm,
  right          = 2.25cm,
  marginparwidth = 2cm,
  marginparsep   = 2pt,
  heightrounded
}

\setlength{\parindent}{0cm}


% == TOC & Co. == %

\renewcommand{\thesection}{\Roman{section}}
\renewcommand{\thesubsection}{\arabic{subsection}}
\renewcommand{\thesubsubsection}{\alph{subsubsection}}

% Source
%  * https://tex.stackexchange.com/a/558025/6880
\DeclareTOCStyleEntries[
  raggedentrytext,
  linefill = \hfill,
  indent   = 0pt,
  dynindent,
  numwidth = 0pt,
  numsep   = 1ex,
  dynnumwidth
]{tocline}{
  chapter,
  section,
  subsection,
  subsubsection,
  paragraph,
  subparagraph
}

\DeclareTOCStyleEntry[indentfollows = chapter]{tocline}{section}


% == COLOR TRANSFORMATIONS == %

%%%
% prototype::
%     #1 : (black-rate)
%          the amount of color relative to black.
%     #2 : (color)
%          one color following the ''color'' format.
%
%     :return: a "darker" version of the color ''#1''.
%%%
\NewExpandableDocumentCommand{\tdocdarkcolor}{ O{50} m }{#2!#1!black}


%%%
% prototype::
%     #1 : (transparency)
%          the transparency rate.
%     #2 : (color)
%          one color following the ''color'' format.
%
%     :return: a "transparent" version of the color `#1`.
%%%
\NewExpandableDocumentCommand{\tdoclightcolor}{ O{5} m }{#2!#1}


% == ICONS == %

%%%
% prototype::
%     #1 : (aws-icon)
%          one material that expects to be an icon command from the
%          ''fontawsome5'' \pack.
%
%     :return: the icon followed by a small insecable space.
%%%
\NewDocumentCommand{\tdocicon}{ m }{%
  #1\kern.45em%
}


% == FOR LISTINGS == %

%%%
% ????
%%%
\newif\ifcodenolexer
\codenolexerfalse


\ExplSyntaxOn

%%%
% prototype::
%     #1 : (style-abbrev)
%          a shortcut for a \tcolorbox styling command.
%        @ #1 in [code, sbs, std]
%
% In the following easy-to-understand macro, we use one fictive \tcolorbox
% style such as to indicate an unknown ''tutodoc'' shortcut style. For example,
% this will give the following message if the user type ''MISTYPED-STYLE''.
%
% term::
%     Package pgfkeys Error: I do not know the key '/tcb/[[tutodoc : tdoclatex
%     bad option "MISTYPED-STYLE"]]' and I am going to ignore it. Perhaps you
%     misspelled it.
%
%     See the pgfkeys package documentation for explanation.
%%%

\NewExpandableDocumentCommand{\tdoctcb}{m}{
  \str_case:nnF { #1 } {
    { sbs  } { listing ~ side ~ text }
    { code } { listing ~ only }
    { std  } { listing ~ and ~ text }
  } {
    [[tutodoc ~ : ~ LaTeX ~ listing ~ illegal ~ style ~ "#1"]]
  }
}

\ExplSyntaxOff


% == THEME == %

\input{../main/css/\tutodoc@theme.cls.sty}

\pagecolor{tutodoc@page@color}
\color{tutodoc@text@color}

\hypersetup{
  colorlinks,
  citecolor = tutodoc@link@color,
  filecolor = tutodoc@link@color,
  linkcolor = tutodoc@link@color,
  urlcolor  = tutodoc@link@color
}
