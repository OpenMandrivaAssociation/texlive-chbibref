Name:		texlive-chbibref
Version:	17120
Release:	1
Summary:	Change the Bibliography/References title
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chbibref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chbibref.r17120.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chbibref.doc.r17120.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a single command, \setbibref, which sets whichever of
\bibname and \refname is in use. (\bibname is used in book.cls
and report.cls, and \refname is used in article.cls.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chbibref/chbibref.sty
%doc %{_texmfdistdir}/doc/latex/chbibref/chbibref.pdf
%doc %{_texmfdistdir}/doc/latex/chbibref/chbibref.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
