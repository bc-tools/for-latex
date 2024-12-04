% -- COLORFUL HIGHLIGHTING OF CONTENT -- %

\NewExpandableDocumentCommand{\tutodoc@build@title@color}{m}{%
  white%
}

\NewExpandableDocumentCommand{\tutodoc@build@upper@color}{m}{%
  \tdocdarkcolor[40]{Gray}%
}

\NewExpandableDocumentCommand{\tutodoc@build@back@color}{m}{%
  \tdoclightcolor[10]{Gray}%
}

\NewExpandableDocumentCommand{\tutodoc@build@frame@color}{m}{%
  Gray!75!black!45%
}

\colorlet{tutodoc@admonition@shadow@color}{Gray!15}


\ExplSyntaxOn

%%%
% We use two ''prop'' variables to factorize the code just after.
%%%
\prop_new:N \g__tutodoc_focus_color_prop
\prop_new:N \g__tutodoc_focus_icon_prop

\prop_set_from_keyval:Nn \g__tutodoc_focus_color_prop {
  note = DarkGray,
  tip  = DarkGray,
  imp  = DarkGray,
  caut = DarkGray,
  warn = DarkGray,
}

\prop_set_from_keyval:Nn \g__tutodoc_focus_icon_prop {
  note = \faInfoCircle,
  tip  = \faLightbulb,
  imp  = \faHighlighter,
  caut = \faBiohazard,
  warn = \faSkullCrossbones,
}

\ExplSyntaxOff



% :: LEXER USED :: %

\newcommand{\tutodoc@latex@lexer}{latex}

% :: INLINE LATEX MACRO :: %

\newcommand{\tutodoc@latex@style}{friendly_grayscale}

\colorlet{tutodoc@latex@back@color}{gray!5}
\colorlet{tutodoc@latex@text@color}{black}


% :: THE TCOLORBOX LISTING STYLE :: %

\colorlet{tutodoc@latex@frame@color}{darkgray}

\newcommand{\tutodoc@latex@left@len}{1mm}
\newcommand{\tutodoc@latex@right@len}{1mm}
\newcommand{\tutodoc@latex@top@len}{1mm}
\newcommand{\tutodoc@latex@bottom@len}{1mm}

\newcommand{\tutodoc@latex@arc@len}{.75mm}

\newcommand{\tutodoc@latex@left@rule@len}{1pt}
\newcommand{\tutodoc@latex@right@rule@len}{1pt}
\newcommand{\tutodoc@latex@top@rule@len}{1pt}
\newcommand{\tutodoc@latex@bottom@rule@len}{1pt}

\colorlet{tutodoc@latex@shadow@color}{black!30}
\newcommand{\tutodoc@latex@shadow@xshift@len}{.75mm}
\newcommand{\tutodoc@latex@shadow@yshift@len}{-.75mm}
\newcommand{\tutodoc@latex@shadow@offset@len}{0mm}

\colorlet{tutodoc@latex@segment@color}{gray}



% -- TEXT AND PAGE COLORS -- %

\colorlet{tutodoc@page@color}{white}
\colorlet{tutodoc@text@color}{black}


% -- LINKS COLOR -- %

\definecolor{tutodoc@link@color}{named}{DimGray}



% -- SHOWCASE -- %

\NewExpandableDocumentCommand{\tutodoc@showcase@rule@color}{}{%
  black%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@stripe@color}{}{%
  darkgray%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@text@color}{}{%
  black%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@build@rule@color}{m}{%
  black%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@build@back@color}{m}{%
  gray!10%
}



% -- VERSION & CHANGES -- %

\NewExpandableDocumentCommand{\tutodoc@changes@when@color}{}{%
  gray%
}
