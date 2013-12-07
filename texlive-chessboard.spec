# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/chessboard
# catalog-date 2008-08-17 13:56:26 +0200
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-chessboard
Version:	1.5
Release:	6
Summary:	Print chess boards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chessboard
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chessboard.source.tar.xz
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
%{_texmfdistdir}/tex/latex/chessboard/chessboard-keys-main.sty
%{_texmfdistdir}/tex/latex/chessboard/chessboard-keys-pgf.sty
%{_texmfdistdir}/tex/latex/chessboard/chessboard-pgf.sty
%{_texmfdistdir}/tex/latex/chessboard/chessboard.sty
%doc %{_texmfdistdir}/doc/latex/chessboard/README
%doc %{_texmfdistdir}/doc/latex/chessboard/README.TEXLIVE
#- source
%doc %{_texmfdistdir}/source/latex/chessboard/chessboard-src.dtx
%doc %{_texmfdistdir}/source/latex/chessboard/chessboard.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 750152
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 718049
- texlive-chessboard
- texlive-chessboard
- texlive-chessboard
- texlive-chessboard
- texlive-chessboard

