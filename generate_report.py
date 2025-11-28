import os
import re

# Configuration
questions = [1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 29, 30, 24, 25, 26]
sets = {
    1: 'set_1', 2: 'set_1', 3: 'set_1', 4: 'set_1', 5: 'set_1',
    12: 'set_2', 13: 'set_2', 14: 'set_2', 15: 'set_2', 16: 'set_2',
    29: 'set_3', 30: 'set_3', 24: 'set_3', 25: 'set_3', 26: 'set_3'
}
base_path = r'c:\Users\vivek\Desktop\ATC'
images_path = os.path.join(base_path, 'images')

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"% Error reading {path}: {e}"

def md_to_latex(text):
    # Remove main headers
    text = re.sub(r'^# .*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^## Question.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^## JFLAP Instructions.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^## Solution.*$', '', text, flags=re.MULTILINE)
    
    # Subsections
    text = re.sub(r'^## (.*)$', r'\\subsubsection*{\1}', text, flags=re.MULTILINE)
    
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', text)
    
    # Italics
    text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', text)
    
    # Code
    text = re.sub(r'`(.*?)`', r'\\texttt{\1}', text)
    
    # Lists
    lines = text.split('\n')
    new_lines = []
    in_list = False
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                new_lines.append('\\begin{itemize}')
                in_list = True
            item = line.strip()[2:]
            new_lines.append(f'    \\item {item}')
        else:
            if in_list:
                new_lines.append('\\end{itemize}')
                in_list = False
            new_lines.append(line)
    if in_list:
        new_lines.append('\\end{itemize}')
    text = '\n'.join(new_lines)
    
    # Tables
    # Simple markdown table to latex conversion
    # Assuming | col | col | format
    if '|' in text:
        table_lines = []
        lines = text.split('\n')
        in_table = False
        headers = []
        alignments = []
        
        processed_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.strip().startswith('|'):
                if not in_table:
                    # Start of table
                    in_table = True
                    # Parse headers
                    headers = [c.strip() for c in line.strip('|').split('|')]
                    # Next line is separator | :--- |
                    i += 1
                    if i < len(lines) and lines[i].strip().startswith('|'):
                        # Parse alignments (simplified)
                        alignments = ['l'] * len(headers) # Default to left
                    
                    processed_lines.append('\\begin{center}')
                    processed_lines.append('\\begin{tabular}{|' + '|'.join(['p{0.3\\textwidth}' for _ in headers]) + '|}')
                    processed_lines.append('\\hline')
                    processed_lines.append(' & '.join([f'\\textbf{{{h}}}' for h in headers]) + ' \\\\ \\hline')
                else:
                    # Row
                    cols = [c.strip() for c in line.strip('|').split('|')]
                    processed_lines.append(' & '.join(cols) + ' \\\\ \\hline')
            else:
                if in_table:
                    processed_lines.append('\\end{tabular}')
                    processed_lines.append('\\end{center}')
                    in_table = False
                processed_lines.append(line)
            i += 1
        if in_table:
            processed_lines.append('\\end{tabular}')
            processed_lines.append('\\end{center}')
        text = '\n'.join(processed_lines)

    # Special chars
    # text = text.replace('_', '\\_') # Be careful with math mode
    # Assuming math is in $...$ and we shouldn't escape inside.
    # Simple approach: escape _ outside of $
    
    return text

def get_image_latex(q_num):
    # Find image starting with q{q_num}_
    for f in os.listdir(images_path):
        if f.startswith(f'q{q_num}_') or f.startswith(f'q{q_num}.'):
             return f"""
\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.7\\textwidth]{{{f}}}
    \\caption{{Automaton for Question {q_num}}}
\\end{{figure}}
"""
    return ""

def generate_latex():
    latex = []
    
    # Preamble
    latex.append(r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath, amssymb}
\usepackage{float}
\usepackage{array}
\usepackage{booktabs}
\usepackage{setspace}
\usepackage{xcolor}

\geometry{a4paper, margin=1in}
\graphicspath{{./images/}}

\begin{document}
\onehalfspacing

\section{Introduction}
This report presents the design and analysis of several computational models in the theory of computation, including Finite Automata (FA), Pushdown Automata (PDA), and Turing Machines (TM).
For each language, appropriate computational models are constructed and verified using JFLAP.
The report is organized so that \textbf{each question has its methodology, results, and discussion grouped under Sections 3, 4, and 5 respectively}.

\section{Problem Statements}
\begin{enumerate}
    \item Design a NPDA for $L = \{ a^n b^n | n \ge 1 \}$
    \item Construct DFA for $L = \{ a b^n a^m : n \ge 2, m \ge 3 \}$
    \item DFA for strings ending with '0011', $\Sigma = \{0,1\}$
    \item NPDA for $L = \{ a^n b^m c^{n+m} \}$
    \item Minimal DFA where 'a' is never followed by 'bb'
    \item[12.] NFA for $\{ab, abc\}^*$
    \item[13.] DFA for strings ending with 'abb'
    \item[14.] DFA for strings ending with 'abba'
    \item[15.] DFA/NFA for strings containing ``the''
    \item[16.] DFA/NFA for strings ending with ``ing''
    \item[29.] TM accepting palindromes over $\{a,b\}$
    \item[30.] TM accepting $\{ w w^R \}$
    \item[24.] TM accepting $\{ 0^n 1^n \}$
    \item[25.] TM accepting $\{ 0^n 1^n 2^n \}$
    \item[26.] TM for strings containing substring 001
\end{enumerate}

\section{Methodology}
This section details the construction approach for each question.
""")

    # Methodology Section
    for q in questions:
        latex.append(f"\\subsection{{Methodology for Question {q}}}")
        pre_path = os.path.join(base_path, sets[q], str(q), f'pre_{q}.md')
        content = read_file(pre_path)
        latex.append(md_to_latex(content))
        latex.append(get_image_latex(q))
        latex.append("\\clearpage")

    latex.append(r"""
\section{Results}
This section presents acceptance tables and correctness verification for each question.
""")

    # Results Section
    for q in questions:
        latex.append(f"\\subsection{{Results for Question {q}}}")
        post_path = os.path.join(base_path, sets[q], str(q), f'post_{q}.md')
        content = read_file(post_path)
        latex.append(md_to_latex(content))
        latex.append("\\clearpage")

    latex.append(r"""
\section{Discussion}
This section contains per-question interpretation of correctness and conceptual insights.
""")

    # Discussion Section
    for q in questions:
        latex.append(f"\\subsection{{Discussion for Question {q}}}")
        latex.append(f"The automaton designed for Question {q} successfully recognizes the target language. The construction follows standard theoretical principles, and the verification results confirm that it accepts valid strings and rejects invalid ones as expected.")

    latex.append(r"""
\section{Comparative Analysis}
\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Memory} & \textbf{Language Class} & \textbf{Example} \\ \hline
DFA & None & Regular & Ending with 0011 \\ \hline
PDA & Stack & Context-Free & $a^n b^n$ \\ \hline
TM & Infinite Tape & RE/Type-0 & $0^n1^n2^n$ \\ \hline
\end{tabular}
\end{center}

\section{Conclusion}
This assignment demonstrated practical construction of automata across the Chomsky hierarchy.
Using JFLAP, each automaton was verified using both valid and invalid strings, confirming correctness and deepening understanding of language recognition models.

\section{References}
\begin{thebibliography}{9}
\bibitem{hopcroft}
Hopcroft, Motwani, Ullman. \textit{Introduction to Automata Theory, Languages, and Computation}.

\bibitem{sipser}
Sipser. \textit{Introduction to the Theory of Computation}.

\bibitem{linz}
Linz. \textit{Formal Languages and Automata}.
\end{thebibliography}

\end{document}
""")

    with open(os.path.join(base_path, 'final_report.tex'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(latex))

if __name__ == '__main__':
    generate_latex()
    print("LaTeX generated successfully.")
