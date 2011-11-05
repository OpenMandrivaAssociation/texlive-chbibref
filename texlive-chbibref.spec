# revision 17120
# category Package
# catalog-ctan /macros/latex/contrib/chbibref
# catalog-date 2010-02-23 16:16:11 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-chbibref
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Defines a single command, \setbibref, which sets whichever of
\bibname and \refname is in use. (\bibname is used in book.cls
and report.cls, and \refname is used in article.cls.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chbibref/chbibref.sty
%doc %{_texmfdistdir}/doc/latex/chbibref/chbibref.pdf
%doc %{_texmfdistdir}/doc/latex/chbibref/chbibref.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
