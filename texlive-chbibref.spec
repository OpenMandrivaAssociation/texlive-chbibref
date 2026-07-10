%global tl_name chbibref
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Change the Bibliography/References title
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chbibref
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chbibref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chbibref.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines a single command, \setbibref, which sets whichever of \bibname
and \refname is in use. (\bibname is used in book.cls and report.cls,
and \refname is used in article.cls.)

