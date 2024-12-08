% == ADMONITIONS == %

\ExplSyntaxOn

%%%
% Without icons and colors, we just use a ''seq'' variable to give
% all the suffixes for the environments concerned.
%%%
\seq_new:N \g__tutodoc_focus_color_seq

\seq_set_from_clist:Nn \g__tutodoc_focus_color_seq {
  note,
  tip,
  imp,
  caut,
  warn,
}

\ExplSyntaxOff



% == LISTING - ANY == %

% -- INLINE CODE -- %

% -- FRAMED LISTING (tcolorbox) -- %



% == LISTING - LATEX == %

% -- LEXER USED -- %

\newcommand{\tutodoc@latex@lexer}{text}


% -- INLINE CODE -- %

\newcommand{\tutodoc@latex@style}{default}

\colorlet{tutodoc@latex@back@color}{white}
\colorlet{tutodoc@latex@text@color}{black}


% -- FRAMED LISTING (tcolorbox) -- %

\colorlet{tutodoc@latex@frame@color}{darkgray}

\newcommand{\tutodoc@latex@left@len}{1mm}
\newcommand{\tutodoc@latex@right@len}{1mm}
\newcommand{\tutodoc@latex@top@len}{1mm}
\newcommand{\tutodoc@latex@bottom@len}{1mm}

\newcommand{\tutodoc@latex@arc@len}{0pt}

\newcommand{\tutodoc@latex@left@rule@len}{1pt}
\newcommand{\tutodoc@latex@right@rule@len}{0pt}
\newcommand{\tutodoc@latex@top@rule@len}{0pt}
\newcommand{\tutodoc@latex@bottom@rule@len}{0pt}

\colorlet{tutodoc@latex@shadow@color}{black}
\newcommand{\tutodoc@latex@shadow@xshift@len}{0mm}
\newcommand{\tutodoc@latex@shadow@yshift@len}{0mm}
\newcommand{\tutodoc@latex@shadow@offset@len}{0mm}

\colorlet{tutodoc@latex@segment@color}{black}



% == TEXT AND PAGE COLORS == %

\colorlet{tutodoc@page@color}{white}
\colorlet{tutodoc@text@color}{black}


% == LINKS COLOR == %

\definecolor{tutodoc@link@color}{named}{black}



% == SHOWCASE == %

\NewExpandableDocumentCommand{\tutodoc@showcase@rule@color}{}{%
  black%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@stripe@color}{}{%
  black%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@text@color}{}{%
  black%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@build@rule@color}{m}{%
  black%
}

\NewExpandableDocumentCommand{\tutodoc@showcase@build@back@color}{m}{%
  white%
}



% == VERSION & CHANGES == %

% -- DATE & VERSION -- %

\NewExpandableDocumentCommand{\tutodoc@changes@when@color}{}{%
  black%
}


% -- ENVS FOR CHANGES MADE -- %

%%%
% The draft theme doesn't use any icon.
%%%

% \newcommand{\tutodoc@changes@start@project@icon}{}

\ExplSyntaxOn

\seq_new:N \g__tutodoc_topic_change_seq

\seq_set_from_clist:Nn \g__tutodoc_topic_change_seq {
  break ,
  fix   ,
  new   ,
  prob  ,
  tech  ,
  update,
  todo  ,
}

\ExplSyntaxOff
