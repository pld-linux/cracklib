# TODO: is $(pkgdatadir)/cracklib.magic used for anything?
#       it's already in file database, so maybe just drop it?
#
# Conditional build:
%bcond_with	words	# bigger words database
#
Summary:	Password checking library
Summary(es.UTF-8):	Biblioteca de chequeo de contraseñas
Summary(fr.UTF-8):	Bibliothèque de vérification de mots de passe
Summary(pl.UTF-8):	Biblioteka sprawdzania haseł
Summary(pt_BR.UTF-8):	Biblioteca de checagem de senhas
Summary(ru.UTF-8):	Библиотека проверки паролей
Summary(tr.UTF-8):	Parola denetim kitaplığı
Summary(uk.UTF-8):	Бібліотека перевірки паролів
Name:		cracklib
Version:	2.8.18
%define	words_v	20080507
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/cracklib/%{name}-%{version}.tar.gz
# Source0-md5:	79053ad8bc714a44cd660cb12116211b
Source1:	http://downloads.sourceforge.net/cracklib/%{name}-words-%{words_v}.gz
# Source1-md5:	7fa6ba0cd50e7f9ccaf4707c810b14f1
URL:		http://sourceforge.net/projects/cracklib/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop users
from choosing passwords which would be easy to guess. CrackLib
performs certain tests:

- It tries to generate words from a username and gecos entry and
  checks those words against the password;
- It checks for simplistic patterns in passwords;
- It checks for the password in a dictionary.

CrackLib is actually a library containing a particular C function
which is used to check the password, as well as other C functions.
CrackLib is not a replacement for a passwd program; it must be used in
conjunction with an existing passwd program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you install
CrackLib, you'll also want to install the cracklib-dicts package.

%description -l de.UTF-8
Überprüft Paßwörter auf Sicherheitsmerkmale - Länge, Eindeutigkeit,
Anwesenheit in einer Wörter-Datenbank usw.

%description -l fr.UTF-8
Vérifie les caractéristiques liées à la sécurité des mots de passe -
longueur, unicité, s'ils sont dans une base de mots, etc.

%description -l pl.UTF-8
CrackLib sprawdza hasła pod kątem bezpieczeństwa. Można użyć tej
biblioteki do powstrzymywania użytkowników przed wybieraniem haseł
łatwych do odgadnięcia. CrackLib przeprowadza następujące testy:

- próbuje wygenerować słowa z nazwy użytkownika i wpisu gecos, a
  następnie porównuje je z hasłem
- szuka prostych wzorców w haśle
- szuka hasła w słowniku

CrackLib to biblioteka zawierająca funkcję C służącą do sprawdzania
hasła oraz inne funkcje C. Nie jest to zamiennik programu passwd -
musi być użyty w połączeniu z istniejącym programem passwd.

%description -l pt_BR.UTF-8
Inclui os dicionários cracklib para o padrão /usr/dict/words, assim
como os utilitários necessários para criar dicionários.

%description -l ru.UTF-8
CrackLib проверяет пароли на предмет соответствия некоторым критериям
безопасности. Она может быть использована для предотвращения выбора
пользователями легкоугадываемых паролей. CrackLib производит такие
тесты:

- Генерирует слова из имени пользователя и поля gecos и сравнивает их
  с паролем;
- Ищет в паролях простые шаблоны;
- Проверяет пароль на наличие его в словаре.

CrackLib - это, собственно, библиотека, содержащая специфическую
функцию C для угадывания паролей и некоторые другие функции. Это не
замена программы passwd, ее надо использовать совместно с существующей
программой passwd.

%description -l tr.UTF-8
Parolaların uzunlukları, sistemde tek olmaları, sözcük veri tabanında
bulunmamaları gibi güvenlikle ilgili özelliklerini kontrol eder.

%description -l uk.UTF-8
CrackLib перевіряє паролі на відповідність деяким критеріям безпеки.
Вона може бути використана для запобігання вибору користувачами
паролів, які легко відгадати. Вона виконує такі тести:

- Генерує слова з імені користувача та поля gecos і порівнює їх з
  паролем;
- Шукає в паролях прості шаблони;
- Перевіряє паролі на наявність їх у словнику.

CrackLib - це, власне, бібліотека, що містить специфічну функцію C для
відгадування паролів та деякі інші функції. Це не заміна програми
passwd, її треба використовувати спільно з існуючою програмою passwd.

%package devel
Summary:	Header files and documentation for cracklib
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para cracklib
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla cracklib
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para a cracklib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentation for cracklib.

%description devel -l es.UTF-8
Este paquete contiene los archivos de inclusión y bibliotecas que se
necesitan para desarrollar programas que usan cracklib.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla cracklib.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão e bibliotecas que são
necessários para desenvolver programas que usam a cracklib.

%package static
Summary:	Static cracklib library
Summary(pl.UTF-8):	Statyczna biblioteka cracklib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cracklib library.

%description static -l pl.UTF-8
Statyczna biblioteka cracklib.

%package dicts
Summary:	Standard dictionaries (/usr/share/dict/words)
Summary(de.UTF-8):	Standard-Wörterbücher (/usr/share/dict/words)
Summary(es.UTF-8):	Diccionarios para chequeo de contraseñas
Summary(fr.UTF-8):	Dictionnaires standards (/usr/share/dict/words)
Summary(pl.UTF-8):	Standardowe słowniki (/usr/share/dict/words)
Summary(pt_BR.UTF-8):	Dicionários para checagem de senhas
Summary(ru.UTF-8):	Стандартные словари CrackLib
Summary(tr.UTF-8):	Standart sözlükler (/usr/share/dict/words)
Summary(uk.UTF-8):	Стандартні словники CrackLib
Group:		Applications/System

%description dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words. Cracklib-dicts also
contains the utilities necessary for the creation of new dictionaries.

%description dicts -l de.UTF-8
Enthält die Cracklib-Wörterbücher für die
Standard-/usr/share/dict/Wörter sowie Utilities zum Erstellen neuer
Wörterbücher"

%description dicts -l es.UTF-8
Incluye el diccionario cracklib para el padrón /usr/share/dict/words,
y utilitarios necesarios a creación de nuevos diccionarios.

%description dicts -l fr.UTF-8
Contient les dictionnaires cracklib pour le /usr/share/dict/words
standard, ainsi que les utilitaires nécessaires à la création de
nouveaux dictionnaires.

%description dicts -l pl.UTF-8
Pakiet zawiera słowniki crackliba dla standardowego
/usr/share/dict/words oraz narzędzia do tworzenia nowych słowników.

%description dicts -l pt_BR.UTF-8
Inclui o dicionário cracklib para o padrão /usr/dict/words, bem como
utilitários necessários a criação de novos dicionários.

%description dicts -l ru.UTF-8
Пакет cracklib-dicts включает словари CrackLib. CrackLib будут нужны
словари, соответствующие вашей системе, которые обычно находятся в
/usr/share/dict/words. Cracklib-dicts также содержит утилиты,
необходимые для создания новых словарей.

%description dicts -l tr.UTF-8
/usr/share/dict/words dosyası için 'cracklib' kitaplıklarını ve yeni
sözlükler yaratılması için gerekli yardımcı programları içerir.

%description dicts -l uk.UTF-8
Пакет cracklib-dicts містить словники CrackLib. CrackLib будуть
потрібні словники, що відповідають вашій системі, котрі зазвичай
знаходяться в /usr/share/dict/words. Cracklib-dicts також містить
утиліти, необхідні для створення нових словників.

%package -n python-cracklib
Summary:	Python binding for cracklib
Summary(pl.UTF-8):	Wiązanie Pythona do crackliba
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-cracklib
Python binding for cracklib.

%description -n python-cracklib -l pl.UTF-8
Wiązanie Pythona do crackliba.

%prep
%setup	-q
%if %{with words}
install %{SOURCE1} dicts/
%endif

%build
%configure \
	--with-default-dict=%{_datadir}/dict/cracklib_dict
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod 755 util/cracklib-format
util/cracklib-format dicts/cracklib* | util/cracklib-packer $RPM_BUILD_ROOT%{_datadir}/dict/cracklib_dict

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{sl_SI,sl}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcrack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcrack.so.2
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcrack.so
%{_libdir}/libcrack.la
%{_includedir}/crack.h
%{_includedir}/packer.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcrack.a

%files dicts
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/cracklib-*
%attr(755,root,root) %{_sbindir}/create-cracklib-dict
%{_datadir}/dict/cracklib_dict.*

%files -n python-cracklib
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_cracklibmodule.so
%{python_sitelib}/%{name}.*
