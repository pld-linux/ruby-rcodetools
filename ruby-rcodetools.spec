Summary:	A tiny web framework
Summary(pl.UTF-8):	Mały szkielet aplikacji WWW
Name:		ruby-rcodetools
Version:	0.7.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://eigenclass.org/static/rcodetools/rcodetools-%{version}.tar.gz
# Source0-md5:	7c2c4c6e649cabdc76aee684b76a1f19
URL:		http://eigenclass.org/hiki.rb?rcodetools
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rcodetools is a collection of Ruby code manipulation tools. It
includes xmpfilter and editor-independent Ruby development helper
tools, as well as emacs and vim interfaces.

Currently, rcodetools comprises:
- xmpfilter: automagic Test::Unit assertions/RSpec expectations and
  code annotations
- rct-complete: 100% accurate method/class/constant etc. completion
- rct-doc: document browsing and code navigator
- rct-meth-args: precise method info (meta-prog. aware) and TAGS
  generation

%description -l pl.UTF-8
rcodetools jest zbiorem narzędzi do manipulacji kodem języka Ruby.
Zawiera xmpfilter, niezależne od edytora narzędzia pomocnicze dla
programistów Ruby'ego oraz interfejsy do emacsa i vima.

Obecnie rcodetools zapewnia:
- xmpfilter: automagiczne asercje Test::Unit/oczekiwania RSpec i
  komentowanie kodu
- rct-complete: dokładne w 100% dopełnianie metod/klas/stałych itp.
- rct-doc: przeglądarka dokumentacji i nawigator kodu
- rct-meth-args: precyzyjne generowanie informacji o metodach (z
  uwzględnieniem meta-prog.) oraz TAGS

%prep
%setup -q -n rcodetools-%{version}

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc README* THANKS
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/rcodetools
%{ruby_rubylibdir}/method_analyzer.rb
%{ruby_rubylibdir}/ruby_toggle_file.rb
%{ruby_ridir}/*
