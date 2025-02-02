#
# spec file for package perl-FFI-C-Stat (Version 0.03)
#
# Copyright (c) 124 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define cpan_name FFI-C-Stat
Name:           perl-FFI-C-Stat
Version:        0.03
Release:        0
License:   Artistic-1.0 or GPL-1.0-or-later
Summary:        Object-oriented FFI interface to native stat and lstat
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl-macros-suse
BuildRequires:  perl-generators
BuildRequires:  perl(FFI::Build::MM) >= 0.83
BuildRequires:  perl(FFI::Platypus) >= 1.00
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Ref::Util)
Requires:       perl(FFI::Platypus) >= 1.00
Requires:       perl(Ref::Util)

%description
Perl comes with perfectly good 'stat', 'lstat' functions, however if you
are writing FFI bindings for a library that use the C 'stat' structure, you
are out of luck there. This module provides an FFI friendly interface to
the C 'stat' function, which uses an object similar to File::stat, except
the internals are a real C 'struct' that you can pass into C APIs that need
it.

Supposing you have a C function:

 void
 my_cfunction(struct stat *s)
 {
   ...
 }

You can bind 'my_cfunction' like this:

 use FFI::Platypus 1.00;

 my $ffi = FFI::Platypus->new( api => 1 );
 $ffi->type('object(FFI::C::Stat)' => 'stat');
 $ffi->attach( my_cfunction => ['stat'] => 'void' );

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README
%license LICENSE

%changelog
