# revision 17120
# category Package
# catalog-ctan /macros/latex/contrib/chbibref
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-chbibref
Version:	1.0
Release:	9
Summary:	Change the Bibliography/References title
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chbibref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chbibref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chbibref.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750104
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718036
- texlive-chbibref
- texlive-chbibref
- texlive-chbibref
- texlive-chbibref
- texlive-chbibref

