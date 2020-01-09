#
# Makefile
#
# Copyright (C) 2008  Red Hat, Inc.  All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

VERSION := $(shell awk '/Version:/ { print $$2 }' anaconda-yum-plugins.spec)
RELEASE := $(shell awk '/Release:/ { print $$2 }' anaconda-yum-plugins.spec)

all:
	echo "nothing to make"

install: 
	mkdir -p $(DESTDIR)/etc/yum/pluginconf.d
	install -m 0644 *.conf $(DESTDIR)/etc/yum/pluginconf.d
	mkdir -p $(DESTDIR)/usr/lib/yum-plugins
	install -m 0644 *.py $(DESTDIR)/usr/lib/yum-plugins

clean:
	rm -f *.pyc

tag:
	@git tag -s -a -m "Tag as anaconda-yum-plugins-$(VERSION)-$(RELEASE)" anaconda-yum-plugins-$(VERSION)-$(RELEASE)
	@echo "Tagged as anaconda-yum-plugins-$(VERSION)-$(RELEASE)"

archive: tag
	@git-archive --format=tar --prefix=anaconda-yum-plugins-$(VERSION)/ anaconda-yum-plugins-$(VERSION)-$(RELEASE) | bzip2 -c > anaconda-yum-plugins-$(VERSION).tar.bz2

src: archive
	rpmbuild -ts --nodeps anaconda-yum-plugins-$(VERSION).tar.bz2 || exit 1
	rm -f anaconda-yum-plugins-$(VERSION).tar.bz2

rpmlog:
	@git-log --pretty="format:- %s (%ae)" anaconda-yum-plugins-$(VERSION)-$(RELEASE).. |sed -e 's/@.*)/)/'
	@echo

bumpver:
	@NEWSUBVER=$$((`echo $(VERSION) |cut -d . -f 4` + 1)) ; \
	NEWVERSION=`echo $(VERSION).$$NEWSUBVER |cut -d . -f 1-3,5` ; \
	DATELINE="* `date "+%a %b %d %Y"` `git-config user.name` <`git-config user.email`> - $$NEWVERSION-1"  ; \
	cl=`grep -n %changelog anaconda-yum-plugins.spec |cut -d : -f 1` ; \
	tail --lines=+$$(($$cl + 1)) anaconda-yum-plugins.spec > speclog ; \
	make --quiet rpmlog 2>/dev/null | fold -s -w 77 | while read line ; do \
		if [ ! "$$(echo $$line | cut -c-2)" = "- " ]; then \
			echo "  $$line" ; \
		else \
			echo "$$line" ; \
		fi ; \
	done > newspeclog ; \
	(head -n $$cl anaconda-yum-plugins.spec ; echo "$$DATELINE" ; cat newspeclog ; echo ""; cat speclog) > anaconda-yum-plugins.spec.new ; \
	mv anaconda-yum-plugins.spec.new anaconda-yum-plugins.spec ; rm -f speclog ; rm -f newspeclog ; \
	sed -i "s/Version: $(VERSION)/Version: $$NEWVERSION/" anaconda-yum-plugins.spec

depend:
