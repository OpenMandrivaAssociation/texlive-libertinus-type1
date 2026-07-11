%global tl_name libertinus-type1
%global tl_revision 76891

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for using Libertinus fonts with LaTeX/pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertinus-type1
License:	gpl2 ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides support for use of Libertinus fonts with
traditional processing engines (LaTeX with dvips or dvipdfmx, or
pdfLaTeX).

