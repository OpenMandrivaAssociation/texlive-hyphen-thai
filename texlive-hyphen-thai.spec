%global tl_name hyphen-thai
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	2
Summary:	Thai hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-thai
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-thai.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Thai in LTH and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-thai:
thai loadhyph-th.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-thai:
\addlanguage{thai}{loadhyph-th.tex}{}{2}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-thai:
['thai'] = {
	loader = 'loadhyph-th.tex',
	lefthyphenmin = 2,
	righthyphenmin = 3,
	synonyms = {  },
	patterns = 'hyph-th.pat.txt',
},
TL_HYPHEN_EOF
