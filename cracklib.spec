Summary:	Password checking library
Summary(fr):	Bibliothèque de vérification de mots de passe
Summary(pl):	Biblioteka sprawdzania hase³
Summary(tr):	Parola denetim kitaplýðý
Name:		cracklib
Version:	2.7
Release:	15
License:	Artistic
Group:		Libraries
Source0:	ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/%{name}_%{version}.tgz
Patch0:		%{name}.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-nss.patch
BuildRequires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Checks passwords for security related characteristics - length,
uniqueness, whether they are in a word database, etc.

%description -l de
Überprüft Paßwörter auf Sicherheitsmerkmale - Länge, Eindeutigkeit,
Anwesenheit in einer Wörter-Datenbank usw.

%description -l fr
Vérifie les caractéristiques liées à la sécurité des mots de passe -
longueur, unicité, s'ils sont dans une base de mots, etc.

%description -l pl
Sprawdza has³a pod k±tem bezpieczeñstwa - d³ugo¶æ, unikalno¶æ, czy
wystêpuj± w s³owniu itp.

%description -l tr
Parolalarýn uzunluklarý, sistemde tek olmalarý, sözcük veri tabanýnda
bulunmamalarý gibi güvenlikle ilgili özelliklerini kontrol eder.

%package devel
Summary:	Header files and documentation for cracklib
Summary(pl):	Pliki nag³ówkowe i dokumentacja dla cracklib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cracklib.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja dla cracklib.

%package dicts
Summary:	Standard dictionaries (/usr/share/dict/words)
Summary(de):	Standard-Wörterbücher (/usr/share/dict/words)
Summary(fr):	Dictionnaires standards (/usr/share/dict/words)
Summary(pl):	Standardowe s³owniki (/usr/share/dict/words)
Summary(tr):	Standart sözlükler (/usr/share/dict/words)
Group:		Applications/System

%description dicts
Includes the cracklib dictionaries for the standard /usr/dict/words,
as well as utilities needed to create new dictionaries.

%description dicts -l de
Enthält die Cracklib-Wörterbücher für die
Standard-/usr/share/dict/Wörter sowie Utilities zum Erstellen neuer
Wörterbücher"

%description dicts -l fr
Contient les dictionnaires cracklib pour le /usr/share/dict/words
standard, ainsi que les utilitaires nécessaires à la création de
nouveaux dictionnaires.

%description dicts -l pl
Pakiet zawiera s³owniki cracklib'a dla standardowego
/usr/share/dict/words oraz narzêdzia do tworzenia nowych s³owników.

%description dicts -l tr
/usr/share/dict/words dosyasý için 'cracklib' kitaplýklarýný ve yeni
sözlükler yaratýlmasý için gerekli yardýmcý programlarý içerir.

%prep
%setup	-q -n %{name},%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} all \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT

install cracklib/packer.h $RPM_BUILD_ROOT%{_includedir}

gzip -9nf README MANIFEST LICENCE POSTER HISTORY

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {README,MANIFEST,LICENCE,POSTER}.gz

%attr(755,root,root) %{_libdir}/lib*so.*

%files devel
%defattr(644,root,root,755)
%doc HISTORY.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files dicts
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/dict/cracklib_dict*
