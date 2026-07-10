%global tl_name chessboard
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Print chess boards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chessboard
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers commands to print chessboards. It can print partial
boards, hide pieces and fields, color the boards and put various marks
on the board. It has a lot of options to place pieces on the board.
Using exotic pieces (e.g., for fairy chess) is possible. The
documentation includes an example of an animated chessboard, for those
whose PDF viewer can display animations.

