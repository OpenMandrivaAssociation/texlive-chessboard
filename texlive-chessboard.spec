Name:		texlive-chessboard
Version:	56833
Release:	2
Summary:	Print chess boards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chessboard
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers commands to print chessboards. It can print
partial boards, hide pieces and fields, color the boards and
put various marks on the board. It has a lot of options to
place pieces on the board. Using exotic pieces (e.g., for fairy
chess) is possible. The documentation includes an example of an
animated chessboard, for those whose PDF viewer can display
animations.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chessboard
%doc %{_texmfdistdir}/doc/latex/chessboard
#- source
%doc %{_texmfdistdir}/source/latex/chessboard

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
