% ********************************************************* %
% ** This is file `tutodoc.cls' generated automatically. ** %
% **                                                     ** %
% ** Copyright (C) 2023-2024 by Christophe, BAL          ** %
% **                                                     ** %
% ** This file may be distributed and/or modified under  ** %
% ** the conditions of the GNU 3 License.                ** %
% ********************************************************* %

\ProvidesExplClass
  {tutodoc}
  {2024-12-04}  % Creation: 2023-11-29
  {1.7.0}
  {This package proposes tools for writing "human friendly" documentations of LaTeX packages.}


% =================== %
% == PACKAGES USED == %
% =================== %

% ------------- %
% -- OPTIONS -- %
% ------------- %

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


% ------------------------------------------------- %
% -- OPTIONS FOR PACKAGES IMPORTED BY OTHER ONES -- %
% ------------------------------------------------- %

% xcolor is loaded by minted and tcolorbox.
\PassOptionsToPackage{svgnames}{xcolor}


% ------------- %
% -- IMPORTS -- %
% ------------- %

\RequirePackage{geometry}

\RequirePackage{marginnote}
\RequirePackage{fontawesome5}
\RequirePackage{keytheorems}

\RequirePackage{clrstrip}

% Before the tcolorbox library minted.
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


% =============== %
% == MAIN CODE == %
% =============== %

% --------------------- %
% -- LOCALE SETTINGS -- %
% --------------------- %

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

  \InputIfFileExists{tutodoc-\tdoclang.loc.cls}{}{
    \input{tutodoc-en.loc.cls}

    \msg_critical:nnx { tutodoc ~ (main) }
      { main : unsupported-lang }
      { \tdoclang }
  }

  \makeatother
}

\ExplSyntaxOff


% ----------------------- %
% -- GEOMETRY SETTINGS -- %
% ----------------------- %

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


% --------------- %
% -- TOC & Co. -- %
% --------------- %

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


% --------------------------- %
% -- COLOR TRANSFORMATIONS -- %
% --------------------------- %

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


% ----------- %
% -- ICONS -- %
% ----------- %

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


% ----------- %
% -- THEME -- %
% ----------- %

\input{tutodoc-\tutodoc@theme.css.cls}

\pagecolor{tutodoc@page@color}
\color{tutodoc@text@color}

\hypersetup{
  colorlinks,
  citecolor = tutodoc@link@color,
  filecolor = tutodoc@link@color,
  linkcolor = tutodoc@link@color,
  urlcolor  = tutodoc@link@color
}


% ------------- %
% -- QUOTING -- %
% ------------- %

%%%
% prototype::
%     #1 : (text)
%          a text to quote.
%
% For example, ''\tdocquote{Something}'' prints **"Something"**.
%%%
\NewDocumentCommand{\tdocquote}{m}{%
  \enquote{\emph{#1}}%
}


% ------------------------------ %
% -- EXPLAINING ENGLISH NAMES -- %
% ------------------------------ %

%%%
% prototype::
%     #1 : (EN-text)
%          an english text that will be explained in another \lang.
%
%     :extra: this macro has a star version.
%
% For example, if the language chosen is ''french'', we have
% the following outputs.
%
%     1) ''\tdocinEN{Something}'' prints
%        **"Something" en anglais**.
%
%     2) ''\tdocinEN*{Something}'' just prints
%        **"Something"**.
%
%     3) ''\tdocinEN*{Something} et \tdocinEN{Another thing}''
%        gives
%        **"Something" et "Another thing" en anglais**.
%%%
\NewDocumentCommand{\tdocinEN}{ s m }{%
  \IfBooleanTF{#1}{}{\tutodoc@trans@in@EN}%
% We must activate the English typesetting rules.
  {%
    \tdocquote{\tutodoc@use@english{#2}}%
  }%
}


% --------------------------- %
% -- HIGHLIGHTING CONTENTS -- %
% --------------------------- %

% :::::::::::::::::::::: %
% :: EXAMPLE & REMARK :: %
% :::::::::::::::::::::: %

\ExplSyntaxOn

%%%
% We use a ''seq'' variable to factorize the code just after.
%%%
\seq_new:N             \g__tutodoc_focus_std_seq
\seq_set_from_clist:Nn \g__tutodoc_focus_std_seq {
  exa,
  rem
}


%%%
% Themes define specific vertical spacings.
%%%
\newkeytheoremstyle{tutodoc@admonition@exa@style}{
  spaceabove = \tutodoc@admonition@space@below,
  spacebelow = \tutodoc@admonition@space@below
}

%%%
% prototype::
%     :action: looping over ''\g__tutodoc_focus_std_seq'' to build new
%              numbered theorems sharing the same section level counter.
%              To achieve that, we use the ''\newkeytheorem'' macro from
%              the ''keytheorems'' \pack.
%%%
\seq_map_inline:Nn \g__tutodoc_focus_std_seq {
  \str_if_eq:nnTF { #1 } { exa } {
    \newkeytheorem{tdoc#1}[
      name   = \use:c { tutodoc@trans@#1@title },
      within = section,
      style  = tutodoc@admonition@exa@style
    ]
  } {
    \newkeytheorem{tdoc#1}[
      name       = \use:c { tutodoc@trans@#1@title },
      numberlike = tdocexa,
      style      = tutodoc@admonition@exa@style
    ]
  }

  \cs_set:cpn { the tdoc #1 } { \thesection.\arabic{tdoc#1} }
}

\ExplSyntaxOff


% ::::::::::::::::: %
% :: ADMONITIONS :: %
% ::::::::::::::::: %

%%%
% note::
%     We provide two ways to define admonitions.
%
%         1) ''\g__tutodoc_focus_color_prop'' and ''g__tutodoc_focus_icon_prop''
%         are for iconised and colored frames.
%
%         1) ''\g__tutodoc_focus_color_seq'' is to use a dedicated basic theorem
%         (this should be only useful for the draft theme).
%
% warning::
%     The variables should be defined inside the themes!
%%%
\ifcsundef{g__tutodoc_focus_color_seq}{
%%%
% source::
%     + https://tex.stackexchange.com/a/727022/6880
%     + https://tex.stackexchange.com/a/682332/6880
%     + https://tex.stackexchange.com/a/623232/6880
%%%
  \tcbset{
    tutodoc-focus-color-style/.style = {
% General.
      use color stack, % Must be before breakable!
      breakable,
      enhanced,
% Colors.
      coltitle = \tutodoc@build@title@color{#1},
      colupper = \tutodoc@build@upper@color{#1},
      colback  = \tutodoc@build@back@color{#1},
      colframe = \tutodoc@build@frame@color{#1},
% We want to use the same color for the footnotes in the frame.
      before upper = {\let\default@color\current@color},
% Padding.
      left  = 3pt,
      right = 3pt,
      arc   = 2pt,
% Frame.
      shadow = {.75mm}{-.75mm}{0mm}{tutodoc@admonition@shadow@color},
   }
  }
}{}

\ExplSyntaxOn

\ifcsundef{g__tutodoc_focus_color_seq}{
%%%
% prototype::
%     :action: ''key/value'' iteration over ''\g__tutodoc_focus_color_prop''
%              to build new colorful unumbered theorems. To achieve that,
%              we use a ''tcolorbox'' style given to the ''\newkeytheorem''
%              macro from the ''keytheorems'' \pack, and icons from the
%              ''fontawesome5'' \pack.
%%%
  \prop_map_inline:Nn \g__tutodoc_focus_color_prop {
    \newkeytheorem{tdoc#1}[
      numbered  = false,
% tcolorbox-no-titlebar can be used.
      tcolorbox = {tutodoc-focus-color-style=#2},
      name      = {
        \tdocicon{ \prop_item:Nn \g__tutodoc_focus_icon_prop { #1 } }
        \use:c { tutodoc@trans@#1@title }
      }
    ]
  }
} {
%%%
% prototype::
%     :action: looping over ''\g__tutodoc_focus_color_seq'' to build new
%              numbered theorems sharing the same section level counter.
%              To achieve that, we use the ''\newkeytheorem'' macro from
%              the ''keytheorems'' \pack.
%%%
  \seq_map_inline:Nn \g__tutodoc_focus_color_seq {
    \newkeytheorem{tdoc#1}[
      name       = \use:c { tutodoc@trans@#1@title },
      numberlike = tdocexa,,
      style      = tutodoc@admonition@exa@style,
% Some hooks...
      preheadhook  = \small,
      postheadhook = \leavevmode,
      postfoothook = \normalsize
    ]
  }
}

\ExplSyntaxOff


% ---------------------------------------------- %
% -- NAMES OF PACKAGES, MACROS & ENVIRONMENTS -- %
% ---------------------------------------------- %

%%%
% prototype::
%     #1 : (cls-name)
%          the name of a class
%
%     :action: ''\tdoccls{myclass}'' prints verb::''myclass''.
%%%
\NewDocumentCommand{\tdoccls}{m}{%
  \texttt{#1}%
}


%%%
% prototype::
%     #1 : (pck-name)
%          the name of a package
%
%     :action:''\tdocpack{mypack}'' prints verb::''mypack''.
%%%
\NewDocumentCommand{\tdocpack}{m}{%
  \texttt{#1}%
}


%%%
% prototype::
%     #1 : (cmd-name)
%          the name of a macro
%
%     :action: ''\tdocmacro{mymacro}'' prints verb::''\mymacro''.
%%%
\NewDocumentCommand{\tdocmacro}{m}{%
  \texttt{\textbackslash{}#1}%
}


%%%
% prototype::
%     #1 : (env-options)
%          hard typed options with the good delimiters
%     #2 : (env-name)
%          the name of an environment
%
%     :extra: this macro has a star version.
%
% Here are the four kind of outputs.
%
%     1) ''\tdocenv{myenv}'' prints
%        verb::''\begin{myenv} ... \end{myenv}''.
%
%     2) ''\tdocenv[{<opt1>[mando2]}]{myenv}'' prints
%         verb::''\begin{myenv}<opt1>[mando2] ... \end{myenv}''.
%
%     3) ''\tdocenv*{myenv}'' prints
%        verb::''myenv''.
%
%     4) ''\tdocenv*[{<opt1>[mando2]}]{myenv}'' prints
%        verb::''myenv''.
%%%
\NewDocumentCommand{\tdocenv}{ s O{} m }{%
  \IfBooleanTF{#1}{%
    \texttt{#3}%
  }{%
% Source: https://tex.stackexchange.com/a/703379/6880 .
    \texttt{\string\begin\string{#3\string}#2 %
            \!\!...\@\!\!\! %
            \string\end\string{#3\string}}%
  }%
}


% ------------------------- %
% -- EXPLAINING PREFIXES -- %
% ------------------------- %

\ExplSyntaxOn

% :::::::::::::: %
% :: MESSAGES :: %
% :::::::::::::: %

\msg_set:nnnn { tutodoc ~ (macroenv) }
  { macroenv : prefix-why-bad-format }
  { Bad ~ format, ~ something ~ like ~ ''pre.fix'' ~ expected. }
  { You ~ must ~ use ~ one ~ single ~ point. }


% :::::::::::::::::::: %
% :: PREFIX FROM... :: %
% :::::::::::::::::::: %

\seq_new:N \l__tutodoc_prewhy_parts_seq
\int_new:N \l__tutodoc_prewhy_nbparts_int
\tl_new:N  \l__tutodoc_pretext_tl
\tl_new:N  \l__tutodoc_posttext_tl

%%%
% prototype::
%     #1 : (pre.fix)
%          a prefix and a suffix separated by one colon.
%
%     :action: ''\tdocprewhy{pre.fix}'' prints verb::''pre''.fix.
%%%
\NewDocumentCommand{\tdocprewhy}{m}{%
% Do we have 2 parts?
  \seq_set_split:Nnn \l__tutodoc_prewhy_parts_seq { . } { #1 }

  \int_set:Nn \l__tutodoc_prewhy_nbparts_int
              {\int_eval:n {\seq_count:N \l__tutodoc_prewhy_parts_seq}}

  \if_int_compare:w \l__tutodoc_prewhy_nbparts_int = 2
  \else:
    \msg_error:nn { tutodoc ~ (macroenv) }
      { macroenv : prefix-why-bad-format }
  \fi:

% Let's go.
  \seq_pop:NN \l__tutodoc_prewhy_parts_seq \l__tutodoc_pretext_tl
  \seq_pop:NN \l__tutodoc_prewhy_parts_seq \l__tutodoc_posttext_tl

  \textbf{
    \tdocpre{\tl_use:N \l__tutodoc_pretext_tl}
    \kern.5pt
    \textperiodcentered
    \kern.5pt
    {\tl_use:N \l__tutodoc_posttext_tl}
  }
}

\ExplSyntaxOff


% ::::::::::::::::::::: %
% :: JUST ONE PREFIX :: %
% ::::::::::::::::::::: %

%%%
% prototype::
%     #1 : (pre)
%          just a prefix
%
%     :action: ''\tdocpre{pre}'' only prints verb::''pre''.
%              This can be useful in a case like
%              ''\tdocpre{pre} comes from \tdocprewhy{pre}{fix}''
%              which prints:
%              verb::''pre'' comes from verb::''pre''-fix.
%%%
\NewDocumentCommand{\tdocpre}{m}{%
  \texttt{#1}%
}


% ------------------------ %
% -- GENERAL FORMATTING -- %
% ------------------------ %

% :::::::::::::::::::::::: %
% :: TEXT INSIDE A RULE :: %
% :::::::::::::::::::::::: %

\ExplSyntaxOn

\box_new:N \l__tutodoc_content_box
\dim_new:N \l__tutodoc_content_dim


%%%
% prototype::
%     #1 : (color)
%          the color for the rule and the text
%     #2 : (text)
%          the text surrounded by two horizontal rules
%
%     :action: this macro adds two horizontal lines on either side of the text.
%              The final output is centered.
%
% note::
%     The code used comes from
%     cf::''this post ;
%           https://tex.stackexchange.com/a/604708/6880''.
%%%
\NewDocumentCommand{\tdocruler}{ O{\tutodoc@showcase@rule@color} m }{
  \par
  {
    \centering
      \scriptsize
      \itshape
      \bfseries
      \color{#1}

      \hbox_set:Nn \l__tutodoc_content_box { \,\, #2 \,\, }
      \dim_set:Nn  \l__tutodoc_content_dim {
        .35 \linewidth - .5 \box_wd:N \l__tutodoc_content_box
      }

      \rule[.75pt] { \dim_use:N \l__tutodoc_content_dim }
                   { 2.5pt }
      \box_use:N   \l__tutodoc_content_box
      \rule[.75pt] { \dim_use:N \l__tutodoc_content_dim }
                   { 2.5pt }
      \par
  }
}

\ExplSyntaxOff


% ::::::::::::::::::::::::::: %
% :: INTERNAL ENVIRONMENTS :: %
% ::::::::::::::::::::::::::: %

%%%
% prototype::
%     #1 : (up-text)
%          the descriptive text before the real output
%     #2 : (down-text)
%          the descriptive text after the real output
%     #3 : (color)
%          one color used to set the one for the decorated texts printed
%          corresponding to the two first arguments.
%     #4 : (text color)
%          color of the content
%     #5 : (rule color builder)
%          the macro used to build the color from the user's rule color
%
%     :action: this environment just adds its content processed by \latex
%              between centered materials produced by the macro ''\tdocruler''
%              such as to stress the start and the end of the content.
%%%
\NewDocumentEnvironment{tutodoc@showcase@basic}{ m m m m m }{%
  \tdocruler[#5{#3}]{#1}%
  \nopagebreak\medskip\nopagebreak\color{#4}%
}{%
  \nopagebreak\medskip\nopagebreak%
  \tdocruler[#5{#3}]{#2}%
}


%%%
% prototype::
%     #1 .. #5 : :see: env.tutodoc@showcase@basic
%     #6       : (back color builder)
%                the macro used to build the color from the user's back color
%
%     :action: this environment adds a page-width colored stripe in the
%              background of the environment content processed by \latex.
%              This stripe is preceded and followed by centered materials
%              produced by the macro ''\tdocruler'' such as to stress the
%              start and the end of the content.
%%%
\NewDocumentEnvironment{tutodoc@showcase@colorstrip}{ m m m m m m }{
  \begin{colorstrip}{#6{#3}}%
    \begin{tutodoc@showcase@basic}{#1}{#2}{#3}{#4}{#5}%
}{%
    \end{tutodoc@showcase@basic}%
  \end{colorstrip}
}


\ExplSyntaxOn

% ::::::::::::::::::::::: %
% :: SETTING SOME KEYS :: %
% ::::::::::::::::::::::: %

\tl_new:N   \l_tutodoc_showcase_before_tl
\tl_new:N   \l_tutodoc_showcase_after_tl
\tl_new:N   \l_tutodoc_showcase_stripe_color_tl
\tl_new:N   \l_tutodoc_showcase_text_color_tl
\bool_new:N \l_tutodoc_showcase_no_stripe_bool


%%%
% prototype::
%     col-stripe : the color of the stripe
%     col-text   : the color of the descriptive texts
%     nostripe   : a boolean flag to avoid the use of a stripe
%     before     : the descriptive text before the real output
%     after      : the descriptive text after the real output
%%%
\keys_define:nn { tutodoc / showcase } {
% Colors.
  col-stripe .tl_set:N  = \l_tutodoc_showcase_stripe_color_tl,
  col-stripe .initial:n = \tutodoc@showcase@stripe@color,
  col-text .tl_set:N    = \l_tutodoc_showcase_text_color_tl,
  col-text .initial:n   = \tutodoc@showcase@text@color,
% Stripe?
  nostripe .bool_set:N = \l_tutodoc_showcase_no_stripe_bool,
  nostripe .initial:n  = false,
% Texts.
  before .tl_set:N  = \l_tutodoc_showcase_before_tl,
  before .initial:n = \tutodoc@trans@latex@show@start,
  after  .tl_set:N  = \l_tutodoc_showcase_after_tl,
  after  .initial:n = \tutodoc@trans@latex@show@end,
}


% :::::::::::::::::::::::::::::: %
% :: SHOWCASE FROM TYPED CODE :: %
% :::::::::::::::::::::::::::::: %

% prototype::
%     #1 : (key-val options)
%          :see: \keys_define:nn { tutodoc / showcase }
%
%     :action: this \env formats \latex code, given as an argument,
%              by framing it with texts decorated by ''\tdocruler'',
%              in order to clearly identify a rendering used as an
%              example.
%              It is also possible to have a coloured strip of the width
%              of the page in the background of the content.
%
%     :see: env.tutodoc@showcase@basic ,
%           env.tutodoc@showcase@colorstrip
%%%
\NewDocumentEnvironment{tdocshowcase}{ O{} }{
  \group_begin:
    \keys_set:nn { tutodoc / showcase } { #1 }

    \bool_if:NTF \l_tutodoc_showcase_no_stripe_bool {
      \begin{tutodoc@showcase@basic}
        { \tl_use:N \l_tutodoc_showcase_before_tl }
        { \tl_use:N \l_tutodoc_showcase_after_tl }
        { \tl_use:N \l_tutodoc_showcase_stripe_color_tl }
        { \tl_use:N \l_tutodoc_showcase_text_color_tl }
        { \tutodoc@showcase@build@rule@color }
    }{
      \begin{tutodoc@showcase@colorstrip}
        { \tl_use:N \l_tutodoc_showcase_before_tl }
        { \tl_use:N \l_tutodoc_showcase_after_tl }
        { \tl_use:N \l_tutodoc_showcase_stripe_color_tl }
        { \tl_use:N \l_tutodoc_showcase_text_color_tl }
        { \tutodoc@showcase@build@rule@color }
        { \tutodoc@showcase@build@back@color }
    }
}{
    \bool_if:NTF \l_tutodoc_showcase_no_stripe_bool {
      \end{tutodoc@showcase@basic}
    }{
      \end{tutodoc@showcase@colorstrip}
    }
  \group_end:
}


% :::::::::::::::::::::::: %
% :: SHOWCASE FROM FILE :: %
% :::::::::::::::::::::::: %

\tl_new:N \l__tutodoc_showcase_options_tl


%%%
% prototype::
%     #1 : (key-val options)
%          :see: env.tdocshowcase
%     #2 : (file path)
%          the path of a file
%%%
\NewDocumentCommand{\tdocshowcaseinput}{ O{} m }{
  \group_begin:
    \keys_set_known:nnN { tutodoc / showcase }
      { #1 }
      \l__tutodoc_showcase_options_tl

    \exp_last_unbraced:NNV \tdocshowcase [\l__tutodoc_showcase_options_tl]
      \input{#2}
    \endtdocshowcase
  \group_end:
}

\ExplSyntaxOff


% -------------------- %
% -- LATEX EXAMPLES -- %
% -------------------- %

% ::::::::::::::::::::::: %
% :: INLINE CODE MACRO :: %
% ::::::::::::::::::::::: %

%%%
% See the \doc of the macro ''\newmintinline'' from the package ''minted''
% to have \infos about the macro ''tdoclatexin''.
%%%
\newmintinline[tdoclatexin]{\tutodoc@latex@lexer}{
  bgcolor            = tutodoc@latex@back@color,
  style/.expand once = \tutodoc@latex@style
}


% ::::::::::::::::::::::::::::::::::: %
% :: TCOLORBOX LISTING ENVIRONMENT :: %
% ::::::::::::::::::::::::::::::::::: %

\ExplSyntaxOn

%%%
% prototype::
%     #1 : (tdoclatex-style)
%          a style of formatting for a \latex listing and its output.
%
%     :see: macro.tdoclatex ,
%           macro.tdoclatexinput
%
% In the following easy-to-understand macro, we use one fictive ''tcolorbox''
% style such as to indicate an unknown ''tutodoc'' style to the user.
% For example, this can give one message similar to the following one where
% the user has type ''MISTYPED-STYLE''.
%
% term::
%     Package pgfkeys Error: I do not know the key '/tcb/tutodoc tdoclatex
%     bad option "MISTYPED-STYLE"' and I am going to ignore it. Perhaps you
%     misspelled it.
%
%     See the pgfkeys package documentation for explanation.
%%%
\NewExpandableDocumentCommand{\tutodoc@latex@listing@format@option}{m}{
  \str_case:nnF { #1 } {
    { sbs  } { listing ~ side ~ text }
    { code } { listing ~ only }
    { std  } { listing ~ and ~ text }
  } { tutodoc ~ tdoclatex ~ bad ~ option ~ "#1" }
}

\ExplSyntaxOff

%%%
% refs::
%     + https://tex.stackexchange.com/a/604821/6880
%     + https://tex.stackexchange.com/a/327983/6880
%%%
\tcbset{
  tutodoc-latex-listing-style/.style = {
% General.
    minted language/.expand once = \tutodoc@latex@lexer,
    minted style/.expand once    = \tutodoc@latex@style,
    breakable,
    enhanced,
% Colors.
    colframe = tutodoc@latex@frame@color,
    colback  = tutodoc@latex@back@color,
    colupper = tutodoc@latex@text@color,
    collower = tutodoc@latex@text@color,
% Padding.
    boxsep = 0pt,
    left   = \tutodoc@latex@left@len,
    right  = \tutodoc@latex@right@len,
    bottom = \tutodoc@latex@bottom@len,
    top    = \tutodoc@latex@top@len,
% Frame.
    shadow     = {\tutodoc@latex@shadow@xshift@len}%
                 {\tutodoc@latex@shadow@yshift@len}%
                 {\tutodoc@latex@shadow@offset@len}%
                 {tutodoc@latex@shadow@color},
    arc        = \tutodoc@latex@arc@len,
    leftrule   = \tutodoc@latex@left@rule@len,
    rightrule  = \tutodoc@latex@right@rule@len,
    bottomrule = \tutodoc@latex@bottom@rule@len,
    toprule    = \tutodoc@latex@top@rule@len,
% Separating line.
    segmentation style = {
      tutodoc@latex@segment@color,
      dash pattern = {on 5pt off 2.5pt},
      line width   = .75pt
    },
    #1
  },
}


%%%
% prototype::
%     #1 : (tdoclatex-style)
%          the style to be used (code only, code and output side by side,
%          or the standard style corresponding to the code followed by
%          its output)
%        @ #1 in [code, sbs, std]
%
% note::
%     See the \doc of the macro ''\newtcblisting'' from the package
%     ''tcolorbox'' to have \infos about the environment ''tdoclatex''.
%%%
\newtcblisting{tdoclatex}[1][std]{%
  tutodoc-latex-listing-style = \tutodoc@latex@listing@format@option{#1}
}


% :::::::::::::::::::::::::::::::::::::: %
% :: TCOLORBOX IMPORTED LISTING MACRO :: %
% :::::::::::::::::::::::::::::::::::::: %

%%%
% prototype::
%     #1 : (tdoclatex-style)
%          :see: ''\newtcblisting{tdoclatex}''
%     #2 : (file path)
%          the path of the file to input and format.
%
% note::
%     See the \doc of the macro ''\newtcbinputlisting'' from the package
%     ''tcolorbox'' to have more \infos about the macro ''\tdoclatexinput''.
%%%
\newtcbinputlisting{\tdoclatexinput}[2][std]{
  listing file                = {#2},
  tutodoc-latex-listing-style = \tutodoc@latex@listing@format@option{#1}
}


% -------------------------- %
% -- LATEX REAL USE CASES -- %
% -------------------------- %

\ExplSyntaxOn

% ::::::::::::::::::::: %
% :: SETTING THE KEY :: %
% ::::::::::::::::::::: %

\tl_new:N \l_tutodoc_listing_explain_tl


%%%
% prototype::
%     explain : the text between the code and its highlighted output.
%
%
% note::
%     This key can be used in addition to those of the ''tdocshowcase''
%     \env,
%%%
\keys_define:nn { tutodoc / listing / latexshow } {
  explain .tl_set:N  = \l_tutodoc_listing_explain_tl,
  explain .initial:n = { \tutodoc@trans@this@gives \tutodoc@colon },
}


% ::::::::::::::::::::: %
% :: LATEXSHOW MACRO :: %
% ::::::::::::::::::::: %

\tl_new:N \l__tutodoc_showcase_options_passed_tl


%%%
% prototype::
%     #1 : (key-val options)
%          :see: \keys_define:nn { tutodoc / listing / latexshow } ,
%                \keys_define:nn { tutodoc / showcase }
%     #2 : (file path)
%          the path of a file
%
%     :see: env.tdocshowcase ,
%           macro.tdoclatexinput
%%%
\NewDocumentCommand{\tdoclatexshow}{ O{} m} {
  \group_begin:
    \keys_set_known:nnN { tutodoc / listing / latexshow }
      { #1 }
      \l__tutodoc_showcase_options_passed_tl

    \tdoclatexinput[code]{#2}

    \tl_use:N \l_tutodoc_listing_explain_tl

% Source: https://tex.stackexchange.com/a/696700/6880
    \exp_last_unbraced:NNV \tdocshowcaseinput [\l__tutodoc_showcase_options_passed_tl] {#2}
  \group_end:
}

\ExplSyntaxOff


% -------------------- %
% -- LATEX EXAMPLES -- %
% -------------------- %

% :::::::::::::::::::::::::::::::::::::::::::::: %
% :: STYLES OF THE LISTING ENV. AND THE MACRO :: %
% :::::::::::::::::::::::::::::::::::::::::::::: %


% ::::::::::::::::::::::: %
% :: INLINE CODE MACRO :: %
% ::::::::::::::::::::::: %

% %%%
% % See the \doc of the macro ''\newmintinline'' from the package ''minted''
% % to have \infos about the macro ''tdoclatexin''.
% %%%
% \newmintinline[tdoclatexin]{\tutodoc@latex@lexer}{%
%   bgcolor            = tutodoc@latex@back@color,%
%   style/.expand once = \tutodoc@latex@style     % <-- This needs minted3!
% }


% ::::::::::::::::::::::::::::::::::: %
% :: TCOLORBOX LISTING ENVIRONMENT :: %
% ::::::::::::::::::::::::::::::::::: %

% \ExplSyntaxOn

% %%%
% % prototype::
% %     #1 : (tdoclatex-style)
% %          a style of formatting for a \latex listing and its output.
% %
% %     :see: macro.tdoclatex ,
% %           macro.tdoclatexinput
% %
% % In the following easy-to-understand macro, we use one fictive ''tcolorbox''
% % style such as to indicate an unknown ''tutodoc'' style to the user.
% % For example, this can give one message similar to the following one.
% %
% % term::
% %     Package pgfkeys Error: I do not know the key '/tcb/tdoclatex bad option
% %     "MISTYPED-STYLE"' and I am going to ignore it. Perhaps you misspelled it.
% %
% %     See the pgfkeys package documentation for explanation.
% %%%
% \NewExpandableDocumentCommand{\tutodoc@latex@listing@format@option}{m}{
%   \str_case:nnF { #1 } {
%     { sbs  } { listing ~ side ~ text }
%     { code } { listing ~ only }
%     { std  } { listing ~ and ~ text }
%   } { tdoclatex ~ bad ~ option ~ "#1" }
% }

% \ExplSyntaxOff

% %%
% % source::
% %     + https://tex.stackexchange.com/a/604821/6880
% %     + https://tex.stackexchange.com/a/327983/6880
% %%
% \tcbset{
%   tutodoc-latex-listing-style/.style = {
% % General.
%     minted language/.expand once = \tutodoc@latex@lexer,
%     minted style/.expand once    = \tutodoc@latex@style,
%     breakable,
%     enhanced,
% % Colors.
%     colframe = tutodoc@latex@frame@color,
%     colback  = tutodoc@latex@back@color,
%     colupper = tutodoc@latex@text@color,
%     collower = tutodoc@latex@text@color,
% % Padding.
%     left   = \tutodoc@latex@left@len,
%     right  = \tutodoc@latex@right@len,
%     bottom = \tutodoc@latex@bottom@len,
%     top    = \tutodoc@latex@top@len,
% % Frame.
%     shadow     = {\tutodoc@latex@shadow@xshift@len}%
%                  {\tutodoc@latex@shadow@yshift@len}%
%                  {\tutodoc@latex@shadow@offset@len}%
%                  {tutodoc@latex@shadow@color},
%     arc        = \tutodoc@latex@arc@len,
%     leftrule   = \tutodoc@latex@left@rule@len,
%     rightrule  = \tutodoc@latex@right@rule@len,
%     bottomrule = \tutodoc@latex@bottom@rule@len,
%     toprule    = \tutodoc@latex@top@rule@len,
% % Separating line.
%     segmentation style = {
%       tutodoc@latex@segment@color,
%       dash pattern = {on 5pt off 2.5pt},
%       line width   = .75pt
%     },
%     #1
%   },
% }


% %%%
% % prototype::
% %     #1 : (tdoclatex-style)
% %          the style to be used (code only, code and output side by side,
% %          or the standard style corresponding to the code followed by
% %          its output)
% %        @ #1 in [code, sbs, std]
% %
% % note::
% %     See the \doc of the macro ''\newtcblisting'' from the package
% %     ''tcolorbox'' to have \infos about the environment ''tdoclatex''.
% %%%
% \newtcblisting{tdoclatex}[1][std]{%
%   tutodoc-latex-listing-style = \tutodoc@latex@listing@format@option{#1}
% }


% :::::::::::::::::::::::::::::::::::::: %
% :: TCOLORBOX IMPORTED LISTING MACRO :: %
% :::::::::::::::::::::::::::::::::::::: %

% %%%
% % prototype::
% %     #1 : (tdoclatex-style)
% %          :see: ''\newtcblisting{tdoclatex}''
% %     #2 : (file path)
% %          the path of the file to input and format.
% %
% % note::
% %     See the \doc of the macro ''\newtcbinputlisting'' from the package
% %     ''tcolorbox'' to have more \infos about the macro ''\tdoclatexinput''.
% %%%
% \newtcbinputlisting{\tdoclatexinput}[2][std]{
%   listing file                = {#2},
%   tutodoc-latex-listing-style = \tutodoc@latex@listing@format@option{#1}
% }


% -------------------------- %
% -- LATEX REAL USE CASES -- %
% -------------------------- %

% \ExplSyntaxOn

% ::::::::::::::::::::: %
% :: SETTING THE KEY :: %
% ::::::::::::::::::::: %

% \tl_new:N \l_tutodoc_listing_explain_tl


% %%%
% % prototype::
% %     explain : the text between the code and its highlighted output.
% %
% %
% % note::
% %     This key can be used in addition to those of the ''tdocshowcase''
% %     \env,
% %%%
% \keys_define:nn { tutodoc / listing / latexshow } {
%   explain .tl_set:N  = \l_tutodoc_listing_explain_tl,
%   explain .initial:n = { \tutodoc@trans@this@gives \tutodoc@colon },
% }


% ::::::::::::::::::::: %
% :: LATEXSHOW MACRO :: %
% ::::::::::::::::::::: %

% \tl_new:N \l__tutodoc_showcase_options_passed_tl


% %%%
% % prototype::
% %     #1 : (key-val options)
% %          :see: \keys_define:nn { tutodoc / listing / latexshow } ,
% %                \keys_define:nn { tutodoc / showcase }
% %     #2 : (file path)
% %          the path of a file
% %
% %     :see: env.tdocshowcase ,
% %           macro.tdoclatexinput
% %%%
% \NewDocumentCommand{\tdoclatexshow}{ O{} m} {
%   \group_begin:
%     \keys_set_known:nnN { tutodoc / listing / latexshow }
%       { #1 }
%       \l__tutodoc_showcase_options_passed_tl

%     \tdoclatexinput[code]{#2}

%     \tl_use:N \l_tutodoc_listing_explain_tl

% % Source: https://tex.stackexchange.com/a/696700/6880
%     \exp_last_unbraced:NNV \tdocshowcaseinput [\l__tutodoc_showcase_options_passed_tl] {#2}
%   \group_end:
% }

% \ExplSyntaxOff


% -- CHANGES - WHEN? --%

\ExplSyntaxOn

% :::::::::::::: %
% :: MESSAGES :: %
% :::::::::::::: %

\msg_set:nnnn { tutodoc ~ (version-n-change) }
  { version-n-change : date-bad-format }
  { Bad ~ format ~ for ~ a ~ date. }
  { Use ~ YYYY-MM-DD. }


% ::::::::::::::::: %
% :: MARGIN NOTE :: %
% ::::::::::::::::: %

\reversemarginpar{}

%%%
% prototype::
%     #1 : (color)
%          the color of the margin note
%     #2 : (up-text)
%          the first material (a version number or nothing)
%     #3 : (down-text)
%          the second material (a date or nothing)
%     #4 : (spacing)
%          the last negative vertical spacing for the 2nd rule
%     #5 : (vertical offset)
%          algebraic distance to move vertically the material
%
%     :action: this macro factorizes the printing of the changes
%              in the left margin.
%
%     :see: \__tutodoc_translate_date:n
%%%
\NewDocumentCommand{\tutodoc@new@change@margin}{ m m m m m }{
  \marginnote{
    \color{#1}
    \scriptsize
    \normalfont
    \centering

    \vspace{0pt}
    \rule{1.65cm}{.95pt}
    \vspace{-2.9pt}

    \IfBlankTF{#2}{}{
      \par
        #2\vphantom{Mp}
      \par
    }

    \IfBlankTF{#3}{}{
      \IfBlankTF{#2}{}{
        \vspace{1pt}
      }

      \par
        \__tutodoc_translate_date:n { #3 }
        \vphantom{Mp}
      \par
    }

    \vspace{#4}
    \rule{1.65cm}{.95pt}
  }[#5]
}


%%%
% prototype::
%     #1 : (EN-num-date)
%          a content that should have the numerical English date
%          format ''YYYY-MM-DD''.
%
%     :action: this function checks if we have something like
%              ''YYYY-MM-DD'', and then it calls the function
%              ''\__tutodoc_translate_date_process:w'' to
%              activate the transformation to the locale format.
%
%     :see: \__tutodoc_translate_date_process:w
%%%
\cs_new:Nn \__tutodoc_translate_date:n {
  \regex_match:nnTF { \A \d{1,4} \- \d{2} \- \d{2} \Z } { #1 }{
    \__tutodoc_translate_date_process:w #1 \q_stop
  }{
    \msg_error:nn { tutodoc ~ (version-n-change) }
      { version-n-change : date-bad-format }
  }
}


%%%
% prototype::
%     #1 : (year-extracted)
%          a 1 to 4 digits integer
%     #2 : (month-extracted)
%          a 2 digits integer
%     #3 : (day-extracted)
%          a 2 digits integer
%
%     :action: this function extracts year, month and day in something
%              like ''YYYY-MM-DD'' and then it calls ''\tutodoc@trans@date''
%              to use the format expected for a "localised" date.
%%%
\cs_new:Npn \__tutodoc_translate_date_process:w #1 - #2 - #3 \q_stop {
    \tutodoc@trans@date{#1}{#2}{#3}
}

\ExplSyntaxOff


% :::::::::::::::::::::: %
% :: VERSION AND DATE :: %
% :::::::::::::::::::::: %

\newlength{\tutodoc@version@date@vertical@sep@len}
\setlength{\tutodoc@version@date@vertical@sep@len}{-4.25pt}

\newlength{\tutodoc@version@date@vertical@offset@len}
\setlength{\tutodoc@version@date@vertical@offset@len}{-8pt}


%%%
% prototype::
%     #1 : (color)
%          the color of the margin note
%     #2 : (version)
%          a version number
%     #3 : (date)
%          a date ''YYYY-MM-DD''
%     #4 : (vertical offset)
%          algebraic distance to move vertically the material
%
%     :action: this macro prints a margin note showing a version number
%              below a date, and the optional argument is used to colorize
%              all this text.
%
% warning::
%     The date must use an english formatting like ''2021-07-14''. This allows
%     to parse the date such as to display it following the standard convention
%     of the language chosen when loading the package.
%%%
\NewDocumentCommand{\tdocversion}{ %
  O{\tutodoc@changes@when@color} %
  m %
  O{} %
  D<>{\tutodoc@version@date@vertical@offset@len}%
}{
  \tutodoc@new@change@margin%
    {#1}                                % Color
    {#2}                                % Version
    {#3}                                % Date
    {\tutodoc@version@date@vertical@sep@len} % Last negative vertical spacing
    {#4}                                % Vertical offset
}


% :::::::::: %
% :: DATE :: %
% :::::::::: %

%%%
% prototype::
%     #1 : (color)
%          the color of the margin note
%     #2 : (date)
%          a date ''YYYY-MM-DD''
%     #3 : (vertical offset)
%          algebraic distance to move vertically the material
%
%     :action: this macro is similar to ''\tdocversion'' except that it just
%              prints a date.
%%%
\NewDocumentCommand{\tdocdate}{
  O{\tutodoc@changes@when@color}
  m
  D<>{\tutodoc@version@date@vertical@offset@len}
}{
  \tutodoc@new@change@margin%
    {#1}                             % Color
    {}                               % Version
    {#2}                             % Date
    {\tutodoc@version@date@vertical@sep@len} % Last negative spacing
    {#3}                             % Vertical offset
}


% --------------------- %
% -- CHANGES - WHAT? -- %
% --------------------- %

\ExplSyntaxOn

% :::::::::::::: %
% :: MESSAGES :: %
% :::::::::::::: %

\msg_set:nnnn { tutodoc ~ (version-n-change) }
  { version-n-change : topic-missing-title }
  { Missing ~ title. }
  { One ~ single ~ title ~ must ~ be ~ indicated. }


% ::::::::::::::::::: %
% :: GENERIC TOPIC :: %
% ::::::::::::::::::: %

\tl_new:N \l_tutodoc_topic_what_color_tl
\tl_new:N \l_tutodoc_topic_when_color_tl
\tl_new:N \l_tutodoc_topic_date_tl
\tl_new:N \l_tutodoc_topic_version_tl


%%%
% prototype::
%     col       : the color of the full content of a topic \env
%     col-chges : the color of the material for changes for a topic \env
%     date      : the date of the changes a topic \env
%     version   : the number version of the changes a topic \env
%%%
\keys_define:nn { tutodoc / version-n-change / topic / options } {
% Colors.
  col       .tl_set:N  = \l_tutodoc_topic_what_color_tl,
  col       .initial:n = tutodoc@text@color,
  col-chges .tl_set:N  = \l_tutodoc_topic_when_color_tl,
  col-chges .initial:n = \tutodoc@changes@when@color,
% Date.
  date .tl_set:N  = \l_tutodoc_topic_date_tl,
  date .initial:n = \c_empty_tl,
% Version.
  version .tl_set:N  = \l_tutodoc_topic_version_tl,
  version .initial:n = \c_empty_tl,
}

\tl_new:N \l__tutodoc_topic_all_user_options_tl


%%%
% For theme that use icons, we need a specific paragraph with less
% vertical space consuming.
%%%
\ifcsundef{g__tutodoc_topic_change_seq}{
  \newcommand{\tutodoc@what@change@paragraph}{%
    \@startsection{paragraph}% Define settings for the "paragraph" section
      {4}% Hierarchy level 4 (paragraph)
      {\z@}% No indentation before the title
      {1.5ex \@plus 1ex \@minus .2ex}% Vertical space before:
                                     % 2ex with flexibility (+1ex / -0.2ex)
      {-1em}% Negative spacing after (title slightly aligned to the left)
      {\normalfont\normalsize\bfseries\sffamily}% Style: normal font, normal size, bold text
  }
}{}


%%%
% prototype::
%     #1 : (title)
%          a title that will be followed by a colon.
%     #2 : (aws-icon)
%          one material that expects to be an icon command from the
%          ''fontawsome5'' \pack
%     #3 : (key-val options)
%          :see: \keys_define:nn { tutodoc / version-n-change / topic / options }
%
%     :action: this environment prints some \infos about specific changes
%              achieved in a new version (no special formatting is applied).
%              Key-val options allow to add a date \andor a \nbver with
%              a specific color if needed.
%%%
\NewDocumentEnvironment{tdoctopic}{ m D<>{} O{} }{
  \IfBlankT{#1}{
    \msg_fatal:nn { tutodoc ~ (version-n-change) }
      { version-n-change : topic-missing-title }
  }

  \keys_set:nn { tutodoc / version-n-change / topic / options } { #3 }

  \tl_clear:N      \l__tutodoc_topic_all_user_options_tl
  \tl_set_eq:NN    \l__tutodoc_topic_all_user_options_tl \l_tutodoc_topic_version_tl
  \tl_put_right:Nn \l__tutodoc_topic_all_user_options_tl { \l_tutodoc_topic_date_tl }

  \group_begin:
    \color{\tl_use:N \l_tutodoc_topic_what_color_tl}

    \ifcsundef{g__tutodoc_topic_change_seq}{{}
% Icon used by the theme.
      \tutodoc@what@change@paragraph{
        \color{\tl_use:N \l_tutodoc_topic_what_color_tl}
        \IfBlankF{#2}{\tdocicon{#2}}
        \textsc{#1.}
      }
    }{
% No icon used by the theme.
      \smallskip
      {\bfseries\textsc{#1.}}
    }

% A date and/or a version.
    \exp_args:Ne \IfBlankF{\l__tutodoc_topic_all_user_options_tl}{
      \exp_args:NNee \tutodoc@new@change@margin
        {\l_tutodoc_topic_when_color_tl}
        {\l_tutodoc_topic_version_tl}
        {\l_tutodoc_topic_date_tl}
        {\tutodoc@version@date@vertical@sep@len}
        {\tutodoc@version@date@vertical@offset@len}
    }

    \begin{itemize}
}{
    \end{itemize}
  \group_end:
}


% :::::::::::::::::::::: %
% :: CLASSICAL TOPICS :: %
% :::::::::::::::::::::: %

%%%
% prototype::
%     :see: env.tdoctopic
%
%     :action: ''key/value'' iteration over ''\g__tutodoc_topic_change_prop''
%              to build topic-like \envs using the \env ''tdoctopic''
%              (the title respects the locale settings).
%%%
\ifcsundef{g__tutodoc_topic_change_seq}{
  \prop_map_inline:Nn \g__tutodoc_topic_change_prop {
    \NewDocumentEnvironment{ tdoc#1 } { O{} } {
      \begin{tdoctopic}{ \use:c { tutodoc@trans@chges@#1 } } < #2 > [##1]
    }{
      \end{tdoctopic}
    }
  }
}{
  \seq_map_inline:Nn \g__tutodoc_topic_change_seq {
    \NewDocumentEnvironment{ tdoc#1 } { O{} } {
      \begin{tdoctopic}{ \use:c { tutodoc@trans@chges@#1 } } [##1]
    }{
      \end{tdoctopic}
    }
  }
}


%%%
% prototype::
%     #1 : (color-content)
%          the color of the full content
%     #2 : (short-desc)
%          a short text expected to indicate the very first version of a project.
%
%     :action: the short text printed will be preceded by a pretty anchor icon.
%%%
\NewDocumentCommand{ \tdocstartproj }{ O{tutodoc@text@color} m } {
  \group_begin:
    \color{#1}
    \ifcsundef{g__tutodoc_topic_change_seq}{
% Icon used.
      \tdocicon{\tutodoc@changes@start@project@icon}
    }{
% No icon used.
      \raisebox{4pt}{\bfseries\tiny\textsc{[Init]}}\kern2pt
    }

    #2
  \group_end:
}

\ExplSyntaxOff


% ----------------- %
% -- DECORATIONS -- %
% ----------------- %

% refs::
%    + https://tex.stackexchange.com/a/130529/6880
%      (for the leaders trick)
%    + https://tex.stackexchange.com/a/269887/6880
%      (for the \hrule width)
%    + https://tex.stackexchange.com/a/729710/6880
%      (centering the \hrule)

\newlength{\tutodoc@vertical@space@deco@len}
\setlength{\tutodoc@vertical@space@deco@len}{\dimeval{2\medskipamount+1.25pt}}


%%%
% prototype::
%     :action: this macro draws a centered horizontal rule with a height
%              of qty::''0.75 pt'', and a width equal to half of the current
%              text width, and extra vertical spaces are added above and
%              below the rule.
%
%     :see: len.tutodoc@vertical@space@deco@len
%%%
\newcommand{\tdocsep}{
  \par
  \cleaders
    \vbox to \tutodoc@vertical@space@deco@len{
      \vfill\centerline{\vrule width 0.5\hsize height 0.75pt}\vfill
    }\vskip\tutodoc@vertical@space@deco@len
}
