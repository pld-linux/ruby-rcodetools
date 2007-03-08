Summary:	A tiny web framework
Name:		ruby-rcodetools
Version:	0.4.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://eigenclass.org/static/rcodetools/rcodetools-%{version}.tar.gz
# Source0-md5:	514837196e2a9aab507dd325bc5753af
URL:		http://eigenclass.org/hiki.rb?rcodetools
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
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


%prep
%setup -q -n rcodetools-%{version}

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

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
%{ruby_ridir}/*
