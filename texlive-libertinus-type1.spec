Name:		texlive-libertinus-type1
Version:	72354
Release:	1
Summary:	Support for using Libertinus fonts with LaTeX/pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libertinus-type1
License:	gpl2 ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-type1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinus-type1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides support for use of Libertinus fonts with
traditional processing engines (LaTeX with dvips or dvipdfmx,
or pdfLaTeX).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/libertinus-type1
%{_texmfdistdir}/fonts/vf/public/libertinus-type1
%{_texmfdistdir}/fonts/type1/public/libertinus-type1
%{_texmfdistdir}/fonts/tfm/public/libertinus-type1
%{_texmfdistdir}/fonts/map/dvips/libertinus-type1
%{_texmfdistdir}/fonts/enc/dvips/libertinus-type1
%doc %{_texmfdistdir}/doc/fonts/libertinus-type1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
