%define upstream_name    Dist-Zilla-Plugin-ModuleBuild-XSOrPP
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Add a --pp option to your Build.PL to force an XS-less build
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Most)
BuildArch:	noarch

%description
Use this plugin instead of the regular 'ModuleBuild' plugin. It generates a
_Build.PL_ which accepts a '--pp' flag to forcible disable XS compilation.
Obviously, this is only useful if your module can work without its XS
component.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

