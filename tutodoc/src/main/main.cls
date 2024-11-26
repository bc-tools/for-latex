% == PACKAGES == %

% -- OPTIONS -- %

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


\tl_new:N \l__tutodoc_other_cls_options_tl

\newcommand{ \tutodoc@theme } { color }

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

\PassOptionsToClass{ fontsize = 10pt,  DIV = 12 }{ scrartcl }

\DeclareUnknownKeyHandler[ tutodoc / main / class / options ]{
  \PassOptionsToClass{ \CurrentOption }{ scrartcl }
}

\ProcessKeyOptions[ tutodoc / main / class / options ]

\LoadClass{ scrartcl }

\ExplSyntaxOff


% -- IMPORTS -- %

% :: TO REMOVE :: %

\RequirePackage[svgnames]%
               {xcolor}




% :: USEFUL :: %


\RequirePackage{hyperref}


\RequirePackage{fontawesome5}

\RequirePackage{keytheorems}


\RequirePackage[highlightmode = immediate]% Before the tcolorbox library minted minted
               {minted}

\RequirePackage{tcolorbox}

\tcbuselibrary{minted,
               breakable,
               skins}

% :: LOCALE :: %

\RequirePackage[utf8]{inputenc}% Load 'inputenc' before 'csquotes'
% We delegate the management of quoting to the ''csquotes'' package,
% which takes care of the locale settings.
\RequirePackage{csquotes} % csquotes should be loaded after fvextra, to avoid a warning from the lineno package on input line 36.


\RequirePackage{clrstrip}

\RequirePackage{marginnote}




% == TOOLS == %

% -- XXXX -- %

% https://www.tug.org/pipermail/tex-live/2016-July/038985.html
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}


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
%     :return: the icon followed by a small insecable space.
%%%
\NewDocumentCommand{\tdocicon}{m}{%
  #1\kern.45em%
}


% -- LOCALE SETTINGS -- %

\ExplSyntaxOn

\msg_set:nnnn { tutodoc ~ (main) }
  { main : unsupported-lang }
  {
    unsupported ~ language ~ << ~ #1 ~ >>. %
    ~ %
    We ~ will ~ use ~ << ~ en ~ >>.
  }
  { \msg_see_documentation_text:n { tutodoc } }


% For the English rules for typesetting.
\newcommand{\tutodoc@use@english}{\relax}

% Babel imposes the managment of the colon for our translations.
\newcommand{\tutodoc@colon}{:}

\AtBeginDocument{
% Babel is used.
  \@ifpackageloaded{babel}{
% We must take care of English rules for English contents.
    \renewcommand\tutodoc@use@english{%
      \foreignlanguage{english}%
    }

% We must take care of colons and spacing.
    \iflanguage{french}{
      \renewcommand{\tutodoc@colon}{\babelshorthand{:}}
    }{}
  }{}

% Polyglossia is used.
  \@ifpackageloaded{polyglossia}{
% If polyglossia is used, we must load english if the user has not done it
% (see the ''\tutodoc@use@english'' macro below).
    \iflanguageloaded{english}{}{
      \setotherlanguage{english}
    }
% We must take care of English rules for English contents.
    \renewcommand\tutodoc@use@english{%
      \foreignlanguage{english}%
    }
  }{}%

  \newcommand{\tdoclang}{\BCPdata{language}}

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


% -- GENERAL SETTINGS -- %

\setlength{\parindent}{0cm}


% -- TOC & Co. -- %

\ifcsundef{chapter}%
          {}%
          {\renewcommand{\thechapter}{\Alph{chapter}}}

\renewcommand{\thesection}{\Roman{section}}
\renewcommand{\thesubsection}{\arabic{subsection}}
\renewcommand{\thesubsubsection}{\roman{subsubsection}}

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
