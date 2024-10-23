% == PACKAGES == %

% -- OPTIONS -- %

\ExplSyntaxOn

\tl_new:N \l__tutodoc_remaining_cls_options_tl

\newcommand{ \tutodoc@theme } { color }

\keys_define:nn { tutodoc / main / class / options } {
  theme .choices:nn = {
    bw,
    color,
    dark,
    draft
  } {
    \renewcommand{ \tutodoc@theme } {
      \tl_use:N \l_keys_choice_tl
    }
  },
  unknown .code:n = {
    \tl_set:Nn \l__tutodoc_remaining_cls_options_tl { #1 }
  }
}

\ProcessKeyOptions[tutodoc / main / class / options]

\LoadClass[ \tl_use:N \l__tutodoc_remaining_cls_options_tl ]%
          { article }%
          [ 2022-06-01 ]

\ExplSyntaxOff


% -- IMPORTS -- %

\RequirePackage[svgnames]%
               {xcolor}%
               [2023/11/15]

\RequirePackage[
  top            = 2.5cm,
  bottom         = 2.5cm,
  left           = 2.5cm,
  right          = 2.5cm,
  marginparwidth = 2cm,
  marginparsep   = 2mm,
  heightrounded
]{geometry}%
 [2020-01-02]

\RequirePackage[raggedright]%
               {titlesec}%
               [2021/07/05]

\RequirePackage{tocbasic}

\RequirePackage{xcolor}%
               [2022/06/12]

\RequirePackage{hyperref}%
               [2023-02-07]


% == TOOLS == %

% -- COLOR TRANSFORMATIONS -- %

%%%
% prototype::
%     #1 : (black-rate)
%          the amount of color relative to black.
%     #2 : (color)
%          one color following the ''xcolor'' format.
%
%     :return: a "darker" version of the color ''#1''.
%%%
\NewExpandableDocumentCommand{\tdocdarkcolor}{O{50}m}{#2!#1!black}


%%%
% prototype::
%     #1 : (transparency)
%          the transparency rate.
%     #2 : (color)
%          one color following the ''xcolor'' format.
%
%     :return: a "transparent" version of the color `#1`.
%%%
\NewExpandableDocumentCommand{\tdoclightcolor}{O{5}m}{#2!#1}


% -- ICONS -- %

%%%
% prototype::
%     #1 : (aws-icon)
%          one material that expects to be an icon command from the
%          ''fontawsome5'' \pack.
%
%     :return: the icon followed by a small insecable  space.
%%%
\NewDocumentCommand{\tdocicon}{m}{%
  #1\kern.45em%
}


% -- LOCALE SETTINGS -- %

\ExplSyntaxOn

\msg_set:nnnn { tutodoc ~ (main) }
  { main : unsupported-lang }
  { unsupported ~ language ~ << ~ #1 ~ >>. }
  { \msg_see_documentation_text:n { tutodoc } }


\newcommand{\tutodoc@colon}{:}

\AtBeginDocument{
% We must take care of colons and spacing.
  \@ifpackageloaded{babel}{
    \iflanguage{french}{
      \renewcommand{\tutodoc@colon}{\babelshorthand{:}}
    }{}
  }{}

  \newcommand{\tdoclang}{\BCPdata{language}}

% If the lang is not supported, we emit a warning and just turn
% to the english language.
  \makeatletter

  \InputIfFileExists{../main/tutodoc-locale-main-\tdoclang.cfg.cls.sty}{}{
	  \input{../main/tutodoc-locale-main-en.cfg.cls.sty}

	  \msg_critical:nnx { tutodoc ~ (main) }
        { main : unsupported-lang }
        { \tdoclang }
	}

  \makeatother
}

\ExplSyntaxOff


% -- GENERAL SETTINGS -- %

\setlength{\parindent}{0cm}


% -- TOC & Co. -- %

\ifcsundef{chapter}%
          {}%
          {\renewcommand{\thechapter}{\Alph{chapter}.}}

\renewcommand{\thesection}{\Roman{section}.}
\renewcommand{\thesubsection}{\arabic{subsection}.}
\renewcommand{\thesubsubsection}{\roman{subsubsection}.}

\titleformat{\paragraph}[hang]%
            {\normalfont\normalsize\bfseries}%
            {\theparagraph}{1em}%
            {}

\titlespacing*{\paragraph}%
              {0pt}%
              {3.25ex plus 1ex minus .2ex}%
              {0.5em}

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


% -- LINKS AND CO. -- %

\input{../main/css/main-\tutodoc@theme.cls.sty}

\hypersetup{
  colorlinks,
  citecolor = tutodoc@link@color,
  filecolor = tutodoc@link@color,
  linkcolor = tutodoc@link@color,
  urlcolor  = tutodoc@link@color
}
