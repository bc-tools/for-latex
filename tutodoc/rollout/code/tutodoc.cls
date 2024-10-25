% ********************************************************* %
% ** This is file `tutodoc.cls' generated automatically. ** %
% **                                                     ** %
% ** Copyright (C) 2023-2024 by Christophe BAL           ** %
% **                                                     ** %
% ** This file may be distributed and/or modified under  ** %
% ** the conditions of the GNU 3 License.                ** %
% ********************************************************* %

\ProvidesExplClass
  {tutodoc}
  {2024-10-19}  % Creation: 2023-11-29
  {1.5.0}
  {This LaTeX class proposes tools for writing "human friendly" PDF documentations of LaTeX packages and classes.}


% =================== %
% == PACKAGES USED == %
% =================== %

% ------------- %
% -- OPTIONS -- %
% ------------- %

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


% ------------- %
% -- IMPORTS -- %
% ------------- %

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
               [2023/10/27]

\RequirePackage{tocbasic}

\RequirePackage{xcolor}%
               [2022/06/12]

\RequirePackage{hyperref}% To load after titlesec!
               [2023-02-07]


% We delegate the management of quoting to the ''csquotes'' package,
% which takes care of the locale settings.
\RequirePackage{csquotes}%
               [2022-09-14]


\RequirePackage{fontawesome5}%
               [2022-05-02]

\RequirePackage{keytheorems}%
               [2024/09/19]

\RequirePackage[svgnames]%
               {xcolor}%
               [2023/11/15]

\RequirePackage{tcolorbox}%
               [2024/07/10]

\tcbuselibrary{breakable,
               skins}


\RequirePackage{clrstrip}%
               [2021-08-28]


\RequirePackage[highlightmode = immediate]%
               {minted}%
               [2024/09/22]

\RequirePackage{tcolorbox}%
               [2024/07/10]

\tcbuselibrary{minted,
               breakable,
               skins}


\RequirePackage{fontawesome5}%
               [2022-05-02]

\RequirePackage{marginnote}%
               [2023-09-07]


% =============== %
% == MAIN CODE == %
% =============== %

% --------------------------- %
% -- COLOR TRANSFORMATIONS -- %
% --------------------------- %

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


% ----------- %
% -- ICONS -- %
% ----------- %

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

  \InputIfFileExists{tutodoc-main-locale-\tdoclang.cfg.cls.sty}{}{
	  \input{tutodoc-main-locale-en.cfg.cls.sty}

	  \msg_critical:nnx { tutodoc ~ (main) }
        { main : unsupported-lang }
        { \tdoclang }
	}

  \makeatother
}

\ExplSyntaxOff


% ---------------------- %
% -- GENERAL SETTINGS -- %
% ---------------------- %

\setlength{\parindent}{0cm}


% --------------- %
% -- TOC & Co. -- %
% --------------- %

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


% ------------------- %
% -- LINKS AND CO. -- %
% ------------------- %

\input{css-\tutodoc@theme-main.cls.sty}

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
%     #1 : (text-en)
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
\NewDocumentCommand{\tdocinEN}{s m}{%
  \IfBooleanTF{#1}{% No star used.
    \tdocquote{#2}%
  }{% Star used.
    \tutodoc@trans@in@EN{\tdocquote{#2}}%
  }%
}


% ----------------------------------- %
% -- SOBER HIGHLIGHTING OF CONTENT -- %
% ----------------------------------- %

% :::::::::::::::::::::: %
% :: EXAMPLE & REMARK :: %
% :::::::::::::::::::::: %

\ExplSyntaxOn

%%%
% We use a ''seq'' variable to factorize the code just after.
%%%
\seq_new:N             \__g_tutodoc_focus_std_seq
\seq_set_from_clist:Nn \__g_tutodoc_focus_std_seq {
  exa,
  rem
}


%%%
% prototype::
%     :action: looping over ''\__g_tutodoc_focus_std_seq'' to build new
%              numbered theorems sharing the same section level counter.
%              To achieve that, we use the ''\newkeytheorem'' macro from
%              the ''keytheorems'' \pack.
%%%
\seq_map_inline:Nn \__g_tutodoc_focus_std_seq {
  \str_if_eq:nnTF { #1 } { exa } {
    \newkeytheorem{tdoc#1}[
      name   = \use:c { tutodoc@trans@#1@title },
      within = section,
    ]
  } {
    \newkeytheorem{tdoc#1}[
      name       = \use:c { tutodoc@trans@#1@title },
      numberlike = tdocexa,
    ]
  }

  \cs_set:cpn { the tdoc #1 } { \thesection\arabic{tdoc#1} }
}

\ExplSyntaxOff


% -------------------------------------- %
% -- COLORFUL HIGHLIGHTING OF CONTENT -- %
% -------------------------------------- %

\input{css-\tutodoc@theme-admonitions.cls.sty}


%%%
% note::
%     We provide two ways to define admonitions.
%
%         1) ''\__g_tutodoc_focus_color_prop'' and ''__g_tutodoc_focus_icon_prop''
%         are for iconised and colored frames.
%
%         1) ''\__g_tutodoc_focus_color_seq'' is to use a dedicated basic theorem
%         (this should be only useful for the draft theme).
%
% warning::
%     The variables should be defined inside the themes!
%%%
\ifcsundef{__g_tutodoc_focus_color_seq}{
%%%
% note::
%     The settings used come from the following sources.
%         * https://tex.stackexchange.com/a/727022/6880
%         * https://tex.stackexchange.com/a/682332/6880
%         * https://tex.stackexchange.com/a/623232/6880
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
% Frame.
      shadow = {.75mm}{-.75mm}{0mm}{tutodoc@admonition@shadow@color},
   }
  }
}{}

\ExplSyntaxOn

\ifcsundef{__g_tutodoc_focus_color_seq}{
%%%
% prototype::
%     :action: ''key/value'' iteration over ''\__g_tutodoc_focus_color_prop''
%              to build new colorful unumbered theorems. To achieve that,
%              we use a ''tcolorbox'' style given to the ''\newkeytheorem''
%              macro from the ''keytheorems'' \pack, and icons from the
%              ''fontawesome5'' \pack.
%%%
  \prop_map_inline:Nn \__g_tutodoc_focus_color_prop {
    \newkeytheorem{tdoc#1}[
      numbered  = false,
% tcolorbox-no-titlebar can be used.
      tcolorbox = {tutodoc-focus-color-style=#2},
      name      = {
        \tdocicon{ \prop_item:Nn \__g_tutodoc_focus_icon_prop { #1 } }
        \use:c { tutodoc@trans@#1@title }
      },
    ]
  }
} {
%%%
% prototype::
%     :action: looping over ''\__g_tutodoc_focus_color_seq'' to build new
%              numbered theorems sharing the same section level counter.
%              To achieve that, we use the ''\newkeytheorem'' macro from
%              the ''keytheorems'' \pack.
%%%
  \seq_map_inline:Nn \__g_tutodoc_focus_color_seq {
    \newkeytheorem{tdoc#1}[
      name       = \use:c { tutodoc@trans@#1@title },
      numberlike = tdocexa,
% We could have used
% \AddToHook{env/tdoc#1/before}{\small}
% and
% \AddToHook{env/tdoc#1/after}{\normalsize}.
      preheadhook  = \small,
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
%
% Cleaner code from https://tex.stackexchange.com/a/703379/6880 .
\NewDocumentCommand{\tdocenv}{s O{} m}{%
  \IfBooleanTF{#1}{%
  	\texttt{#3}%
  }{%
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

%%%
% prototype::
%     #1 : (pre.fix)
%          a prefix and a suffix separated by one colon.
%
%     :action: ''\tdocprewhy{pre.fix}'' prints verb::''pre''.fix.
%%%
\NewDocumentCommand{\tdocprewhy}{m}{%
% Do we have 2 parts?
  \seq_set_split:Nnn \l_tmpa_seq { . } { #1 }

  \int_set:Nn \l_tmpa_int
              {\int_eval:n {\seq_count:N \l_tmpa_seq}}

  \if_int_compare:w \l_tmpa_int = 2
  \else:
    \msg_error:nn { tutodoc ~ (macroenv) }
      { macroenv : prefix-why-bad-format }
  \fi:

% Let's go.
  \seq_pop:NN \l_tmpa_seq \l_tmpa_tl
  \seq_pop:NN \l_tmpa_seq \l_tmpb_tl

  \textbf{\tdocpre{\tl_use:N \l_tmpa_tl}\kern.5pt\textperiodcentered\kern.5pt{\tl_use:N \l_tmpb_tl}}
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

\input{css-\tutodoc@theme-showcase.cls.sty}


% :::::::::::::::::::::::: %
% :: TEXT INSIDE A RULE :: %
% :::::::::::::::::::::::: %

\ExplSyntaxOn

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

\NewDocumentCommand{\tdocruler}{O{\tutodoc@showcase@rule@color} m}{
  \par
  {
    \centering
      \scriptsize
      \itshape
      \bfseries
      \color{#1}

      \hbox_set:Nn \l_tmpa_box { \,\, #2 \,\, }
      \dim_set:Nn  \l_tmpa_dim {
        .35 \linewidth - .5 \box_wd:N \l_tmpa_box
      }

      \rule[.75pt] { \dim_use:N \l_tmpa_dim }
                   { 2.5pt }
      \box_use:N   \l_tmpa_box
      \rule[.75pt] { \dim_use:N \l_tmpa_dim }
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
%          one color following the ''xcolor'' format.
%          This color is used to set the one for the decorated texts printed
%          corresponding to the two first arguments.
%     #4 : (text color)
%          XXXXX
%     #5 : (rule color builder)
%          YYY
%
%     :action: this environment just adds its content processed by \latex
%              between centered materials produced by the macro ''\tdocruler''
%              such as to stress the start and the end of the content.
%%%
\NewDocumentEnvironment{tutodoc@showcase@basic}{m m m m m}{
  \tdocruler[#5{#3}]{#1}%
  \nopagebreak\medskip\nopagebreak\color{#4}%
}{
  \nopagebreak\medskip\nopagebreak
  \tdocruler[#5{#3}]{#2}
}


%%%
% prototype::
%     #1 : (up-text)
%          :see: env.tutodoc@showcase@basic
%     #2 : (down-text)
%          :see: env.tutodoc@showcase@basic
%     #3 : (stripe color)
%          :see: env.tutodoc@showcase@basic
%     #4 : (text color)
%          :see: env.tutodoc@showcase@basic
%     #5 : (rule color builder)
%          :see: env.tutodoc@showcase@basic
%     #6 : (back color builder)
%          :see: env.tutodoc@showcase@basic
%
%     :action: this environment adds a page-width colored stripe in the
%              background of the environment content processed by \latex.
%              This stripe is preceded and followed by centered materials
%              produced by the macro ''\tdocruler'' such as to stress the
%              start and the end of the content.
%%%

\NewDocumentEnvironment{tutodoc@showcase@colorstrip}{m m m m m m}{
  \begin{colorstrip}{#6{#3}}
    \begin{tutodoc@showcase@basic}{#1}{#2}{#3}{#4}{#5}
}{
    \end{tutodoc@showcase@basic}
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
\bool_new:N \l_tutodoc_showcase_nostripe_bool


%%%
% We define the key-val options that will be exposed by the \env
% ''tdocshowcase''.
%%%
\keys_define:nn { tutodoc / showcase } {
% Texts.
  before .tl_set:N  = \l_tutodoc_showcase_before_tl,
  before .initial:n = \tutodoc@trans@latex@show@start,
  after  .tl_set:N  = \l_tutodoc_showcase_after_tl,
  after  .initial:n = \tutodoc@trans@latex@show@end,
% Colors.
  colstripe .tl_set:N  = \l_tutodoc_showcase_stripe_color_tl,
  colstripe .initial:n = \tutodoc@showcase@stripe@color,
  coltext .tl_set:N    = \l_tutodoc_showcase_text_color_tl,
  coltext .initial:n   = \tutodoc@showcase@text@color,
% Stripe?
  nostripe .bool_set:N = \l_tutodoc_showcase_nostripe_bool,
  nostripe .initial:n  = false,
}


% :::::::::::::::::::::::::::::: %
% :: SHOWCASE FROM TYPED CODE :: %
% :::::::::::::::::::::::::::::: %

% prototype::
%     #1 : (key-val)
%          the key-value options (see above).
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

    \bool_if:NTF \l_tutodoc_showcase_nostripe_bool {
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
    \bool_if:NTF \l_tutodoc_showcase_nostripe_bool {
      \end{tutodoc@showcase@basic}
    }{
      \end{tutodoc@showcase@colorstrip}
    }
  \group_end:
}


% :::::::::::::::::::::::: %
% :: SHOWCASE FROM FILE :: %
% :::::::::::::::::::::::: %

%%%
% prototype::
%     #1 : (key-val)
%          :see: env.tdocshowcase
%     #2 : (file-path)
%          the path of a file
%%%
\NewDocumentCommand{\tdocshowcaseinput}{O{} m}{
  \group_begin:
    \keys_set_known:nnN { tutodoc / showcase }
      { #1 }
      \l_tmpa_tl

    \exp_last_unbraced:NNV \tdocshowcase [\l_tmpa_tl]
      \input{#2}
    \endtdocshowcase
  \group_end:
}

\ExplSyntaxOff


% -------------------- %
% -- LATEX EXAMPLES -- %
% -------------------- %

% :::::::::::::::::::::::::::::::::::::::::::::: %
% :: STYLES OF THE LISTING ENV. AND THE MACRO :: %
% :::::::::::::::::::::::::::::::::::::::::::::: %

\newcommand{\tutodoc@latex@lexer}{latex}

\input{css-\tutodoc@theme-listing.cls.sty}


% :::::::::::::::::::::::: %
% :: INLINE LATEX MACRO :: %
% :::::::::::::::::::::::: %

%%%
% See the \doc of the macro ''\newmintinline'' from the package ''minted''
% to have \infos about the macro ''tdocinlatex''.
%%%
\newmintinline[tdocinlatex]{\tutodoc@latex@lexer}{%
  bgcolor            = tutodoc@latex@back@color,%
  style/.expand once = \tutodoc@latex@style% <-- This needs minted3!
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
% For example, this can give one message similar to the following one.
%
% term::
%     Package pgfkeys Error: I do not know the key '/tcb/tdoclatex bad option
%     "MISTYPED-STYLE"' and I am going to ignore it. Perhaps you misspelled it.
%
%     See the pgfkeys package documentation for explanation.
%%%
\NewExpandableDocumentCommand{\tutodoc@latex@listing@formating}{ m }{
  \str_case:nnF { #1 } {
    { sbs  } { listing ~ side ~ text }
    { code } { listing ~ only }
    { std  } { listing ~ and ~ text }
  } { tdoclatex ~ bad ~ option ~ "#1" }
}

\ExplSyntaxOff

%%
% source::
%     + https://tex.stackexchange.com/a/604821/6880
%     + https://tex.stackexchange.com/a/327983/6880
%%
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
    left   = \tutodoc@latex@left,
    right  = \tutodoc@latex@right,
    bottom = \tutodoc@latex@bottom,
    top    = \tutodoc@latex@top,
% Frame.
    shadow     = {\tutodoc@latex@shadow@xshift}%
                 {\tutodoc@latex@shadow@yshift}%
                 {\tutodoc@latex@shadow@offset}%
                 {tutodoc@latex@shadow@color},
    arc        = \tutodoc@latex@arc,
    leftrule   = \tutodoc@latex@left@rule,
    rightrule  = \tutodoc@latex@right@rule,
    bottomrule = \tutodoc@latex@bottom@rule,
    toprule    = \tutodoc@latex@top@rule,
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
  tutodoc-latex-listing-style = \tutodoc@latex@listing@formating{#1}
}


% :::::::::::::::::::::::::::::::::::::: %
% :: TCOLORBOX IMPORTED LISTING MACRO :: %
% :::::::::::::::::::::::::::::::::::::: %

%%%
% prototype::
%     #1 : (tdoclatex-style)
%          :see: ''\newtcblisting{tdoclatex}''
%     #2 : (file-path)
%          the path of the file to input and format.
%
% note::
%     See the \doc of the macro ''\newtcbinputlisting'' from the package
%     ''tcolorbox'' to have more \infos about the macro ''\tdoclatexinput''.
%%%
\newtcbinputlisting{\tdoclatexinput}[2][std]{
  listing file                = {#2},
  tutodoc-latex-listing-style = \tutodoc@latex@listing@formating{#1}
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
%     :see: macro.tdoclatexshow
%
% We add a key-val option specific to ''\tdoclatexshow'', the other ones
% will be sent to ''\tdocshowcaseinput''.
%%%
\keys_define:nn { tutodoc / listing / latexshow } {
  explain .tl_set:N  = \l_tutodoc_listing_explain_tl,
  explain .initial:n = { \tutodoc@trans@this@gives \tutodoc@colon },
}


% ::::::::::::::::::::: %
% :: LATEXSHOW MACRO :: %
% ::::::::::::::::::::: %

%%%
% prototype::
%     #1 : (key-val)
%          the key-value options supported by the ''tdocshowcase'' \env,
%          plus one allowing you to change the description of a line
%          printed between the code and its highlighted output.
%     #2 : (file-path)
%          the path of a file
%
%     :see: env.tdocshowcase ,
%           macro.tdoclatexinput
%%%
\NewDocumentCommand{\tdoclatexshow}{O{} m}{
  \group_begin:
    \keys_set_known:nnN { tutodoc / listing / latexshow }
      { #1 }
      \l_tmpa_tl

    \tdoclatexinput[code]{#2}

    \tl_use:N \l_tutodoc_listing_explain_tl

% Source: https://tex.stackexchange.com/a/696700/6880
    \exp_last_unbraced:NNV \tdocshowcaseinput [\l_tmpa_tl] {#2}
  \group_end:
}

\ExplSyntaxOff


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
%
%     :action: this macro factorizes the printing of the changes
%              in the left margin.
%
%     :see: \__tutodoc_translate_date:n
%%%
\NewDocumentCommand{\tutodoc@new@change@margin}{m m m m}{
  \marginnote{
    \color{#1}
    \scriptsize
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
        \__tutodoc_translate_date:n { #3 }\vphantom{Mp}
      \par
    }

    \vspace{#4}
    \rule{1.65cm}{.95pt}
  }[-.345cm]
}


%%%
% prototype::
%     :action: this function checks if we have something like
%              ''YYYY-MM-DD'' and then it calls the function
%              ''\__tutodoc_translate_date_process:w'' to finish
%              the job.
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
%     :action: this function extracts year, month and day in something
%              like ''YYYY-MM-DD'' and then it calls ''\tutodoc@trans@date''
%              to use the format expected for a "localised" date.
%%%
\cs_new:Npn \__tutodoc_translate_date_process:w #1 - #2 - #3 \q_stop {
    \tutodoc@trans@date{#1}
                       {#2}
                       {#3}
}

\ExplSyntaxOff


% :::::::::::::::::::::: %
% :: VERSION AND DATE :: %
% :::::::::::::::::::::: %

\input{css-\tutodoc@theme-version-n-change.cls.sty}

%%%
% prototype::
%     #1 : (color)
%          the color of the margin note
%     #2 : (version)
%          a version number
%     #3 : (date)
%          a date ''YYYY-MM-DD''
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
\NewDocumentCommand{\tdocversion}{O{\tutodoc@changes@version@color} m O{}}{
  \tutodoc@new@change@margin{#1}      % Color
                            {#2}      % Version
                            {#3}      % Date
                            {-4.25pt} % Last negative vertical spacing
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
%
%     :action: this macro is similar to ''\tdocversion'' except that it just
%              prints a date.
%%%
\NewDocumentCommand{\tdocdate}{O{\tutodoc@changes@date@color} m}{
  \tutodoc@new@change@margin{#1}      % Color
                            {}        % Version
                            {#2}      % Date
                            {-5.35pt} % Last negative spacing
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


% ::::::::::::::::::::: %
% :: CHANGES - TOPIC :: %
% ::::::::::::::::::::: %

%%%
% prototype::
%     #1 : (title)
%          a title that will be followed by a colon.
%     #2 : (aws-icon)
%          one material that expects to be an icon command from the
%          ''fontawsome5'' \pack.
%
%     :action: this environment prints some \infos about specific changes
%              achieved in a new version (no special formatting is applied).
%%%
\NewDocumentEnvironment{tdoctopic}{ m O{} }{
  \IfBlankT{#1}{
    \msg_fatal:nn { tutodoc ~ (version-n-change) }
      { version-n-change : topic-missing-title }
  }%
  \textbf{%
    \IfBlankF{#2}{\tdocicon{#2}}%
    \textsc{#1.}
  }

  \begin{itemize}
}{
  \end{itemize}
}


% :::::::::::::::::::::::::: %
% :: CHANGES - NEW THINGS :: %
% :::::::::::::::::::::::::: %

%%%
% We use a ''prop'' variable to factorize the code just after.
%%%
\prop_new:N              \__g_tutodoc_topic_change_prop
\prop_set_from_keyval:Nn \__g_tutodoc_topic_change_prop {
  break  = \faCodeBranch,
  fix    = \faWrench,
  new    = \faGem,
  prob   = \faFire*,
  tech   = \faFlask,
  update = \reflectbox{\faHistory},
}


%%%
% prototype::
%     :see: env.tdoctopic
%
%     :action: ''key/value'' iteration over ''\__g_tutodoc_topic_change_prop''
%              to build topic-like \envs using the \env ''tdoctopic''
%              (the title used is translated into the good language).
%%%
\prop_map_inline:Nn \__g_tutodoc_topic_change_prop {
  \NewDocumentEnvironment{ tdoc#1 } {} {
    \begin{tdoctopic}{ \use:c { tutodoc@trans@chges@#1 } } [ #2 ]
  }{
    \end{tdoctopic}
  }
}


%%%
% prototype::
%     #1 : (short-desc)
%          a short text expected t indicate the very first version of a project.
%
%     :action: the short text printed will be preceded by a pretty anchor icon.
%%%
\NewDocumentCommand{ \tdocstartproj }{ m } {
  \tdocicon{\faAnchor}#1
}

\ExplSyntaxOff


% ----------------- %
% -- DECORATIONS -- %
% ----------------- %

% Source
%    * https://tex.stackexchange.com/a/705938/6880
%      (for \addvspace{\medskipamount} instead of \medskip)

%%%
% prototype::
%     :action: this macro draws a centered horizontal rule with a height
%              of qty::''0.75 pt'', and a width equal to half of the current
%              text width, and extra vertical spaces are added above and 
%              below the rule.
%%%
\NewDocumentCommand{\tdocsep}{}{
  \par\addvspace{\medskipamount}
  \hfill\rule{0.5\textwidth}{0.75pt}\hfill\null
  \medskip
  \smallskip
}
