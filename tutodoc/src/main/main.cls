% == PACKAGES == %

\LoadClassWithOptions{article}[2022-06-01]

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

% -- LOCALE SETTINGS -- %

\ExplSyntaxOn

\msg_set:nnnn { tutodoc } { unsupported-lang }
  { unsupported ~ language ~ << ~ #1 ~ >>. }
  { \msg_see_documentation_text:n {tutodoc} }


\newcommand{\tutodoc@colon}{:}

\AtBeginDocument{
% We must take care of the colons, babel and spacing.
  \@ifpackageloaded{babel}{
  \iflanguage{french}{
      \renewcommand{\tutodoc@colon}{\babelshorthand{:}}
    }{}
  }{}

  \newcommand{\tdoclang}{\BCPdata{language}}

% If the lang is not supported, we emit a warning and just turn 
% to the english language.
  \makeatletter
  	\InputIfFileExists{../main/tutodoc-locale-main-\tdoclang.cfg.sty}{}{
	  \input{../main/tutodoc-locale-main-en.cfg.sty}

	  \msg_warning:nnx { tutodoc } { unsupported-lang }
        { \tdoclang }
	}
  \makeatother
}

\ExplSyntaxOff
  
  
% -- GENERAL SETTINGS -- %

\setlength{\parindent}{0cm}


% -- LINKS -- %

\newcommand{\tdoclinkcolor}{NavyBlue!85!white}

\hypersetup{
  colorlinks,
  citecolor = \tdoclinkcolor,
  filecolor = \tdoclinkcolor,
  linkcolor = \tdoclinkcolor,
  urlcolor  = \tdoclinkcolor
}


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


% -- COLOR TRANSFORMATIONS -- %

%%%
% prototype::
%     #1 : the amount of color relative to black.
%     #2 : one color following the ''xcolor'' format.
%
%     :return: a "darker" version of the color ''#1''.
%%%
\NewExpandableDocumentCommand{\tdocdarkcolor}{O{50}m}{#2!#1!black}


%%%
% prototype::
%     #1 : the transparency rate.
%     #2 : one color following the ''xcolor'' format.
%
%     :return: a "transparent" version of the color `#1`.
%%%
\NewExpandableDocumentCommand{\tdoclightcolor}{O{5}m}{#2!#1}


% -- ICONS -- %

%%%
% prototype::
%     #1 : one material that expects to be an icon command from the
%          ''fontawsome5'' \pack.
%
%     :return: the icon followed by a small insecable  space.
%%%
\NewDocumentCommand{\tdocicon}{m}{%
  #1\kern.45em%
}
