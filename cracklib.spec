Summary:     Password checking library
Summary(fr): Bibliothèque de vérification de mots de passe
Summary(tr): Parola denetim kitaplýðý
Name:        cracklib
Version:     2.7
Release:     3
Group:       Development/Libraries
Source:      ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/%{name}_%{version}.tgz
URL:         ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/
Copyright:   artistic
Patch:       cracklib-2.7-redhat.patch
Buildroot:   /tmp/%{name}-%{version}-root

%description
Checks passwords for security related characteristics - length, uniqueness, 
whether they are in a word database, etc.

%description -l de
Überprüft Paßwörter auf Sicherheitsmerkmale - Länge, Eindeutigkeit, 
Anwesenheit in einer Wörter-Datenbank usw.

%description -l fr
Vérifie les caractéristiques liées à la sécurité des  mots de passe - longueur,
unicité, s'ils sont dans une base de mots, etc.

%description -l tr
Parolalarýn uzunluklarý, sistemde tek olmalarý, sözcük veri tabanýnda
bulunmamalarý gibi güvenlikle ilgili özelliklerini kontrol eder.

%package devel
Summary:     Header files and documentation for cracklib
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
Header files and documentation for cracklib.

%package dicts
Summary:     Standard dictionaries (/usr/dict/words)
Summary(de): Standard-Wörterbücher (/usr/dict/words)
Summary(fr): Dictionnaires standards (/usr/dict/words)
Summary(tr): Standart sözlükler
Group:       Utilities/System

%description dicts
Includes the cracklib dictionaries for the standard /usr/dict/words, as
well as utilities needed to create new dictionaries.

%description -l de dicts
Enthält die Cracklib-Wörterbücher für die Standard-/usr/dict/Wörter sowie
Utilities zum Erstellen neuer Wörterbücher"

%description -l fr dicts
Contient les dictionnaires cracklib pour le /usr/dict/words standard, ainsi
que les utilitaires nécessaires à la création de nouveaux dictionnaires.

%description -l tr dicts
/usr/dict/words dosyasý için 'cracklib' kitaplýklarýný ve yeni sözlükler
yaratýlmasý için gerekli yardýmcý programlarý içerir.


%prep
%setup -q -n %{name},%{version}
%patch -p1

%build
make all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{sbin,lib,include}
make install ROOT=$RPM_BUILD_ROOT

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc README MANIFEST LICENCE POSTER
%attr(755, root, root) /usr/lib/lib*so.*.*

%files devel
%defattr(644, root, root, 755)
%doc HISTORY
%attr(755, root, root) /usr/lib/lib*so
/usr/include/*

%files dicts
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/sbin/*
/usr/lib/cracklib_dict*

%changelog
* Sat Aug 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.7-3]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source and %setup,
- added stripping shared libraries,
- added devel subpackage,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.7
- build shared libraries

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added -fPIC

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- basic spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
