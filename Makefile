VERSION=$(shell python setup.py --version)
DOCKER_RUN = docker run -t -e SSH_AUTH_SOCK -v $(CURDIR):/work:rw
UID:=$(shell id -u)
GID:=$(shell id -g)

.PHONY : all clean tests docs dev

-usage:
	@echo "make test - Run tests"
	@echo "make deb_trusty - Generate trusty deb package"
	@echo "make itest_trusty - Run tests and integration checks"
	@echo "make _itest_trusty - Run only integration checks"
	@echo "make release - Prepare debian info for new release"
	@echo "make clean - Get rid of scratch and byte files"
	@echo "make dev - Get a local copy of trond running in debug mode in the foreground"

docker_%:
	@echo "Building docker image for $*"
	[ -d dist ] || mkdir -p dist
	cd ./yelp_package/$* && docker build -t tron-builder-$* .

deb_%: clean docker_% coffee_%
	@echo "Building deb for $*"
	$(DOCKER_RUN) tron-builder-$* /bin/bash -c ' \
		dpkg-buildpackage -d &&                   \
		mv ../*.deb dist/ &&                      \
		chown -R $(UID):$(GID) dist debian        \
	'

coffee_%:
	@echo "Building tronweb"
	$(DOCKER_RUN) tron-builder-$* /bin/bash -c '      \
		rm -rf tronweb/js/cs &&                      \
		mkdir -p tronweb/js/cs &&                      \
		coffee -o tronweb/js/cs/ -c tronweb/coffee/ && \
		chown -R $(UID):$(GID) tronweb/js/cs/          \
	'

test:
	tox

_itest_%:
	$(DOCKER_RUN) tron-builder-$* /work/itest.sh

itest_%: test deb_% _itest_%
	@echo "Package for $* looks good"

dev:
	.tox/py27/bin/trond --debug --working-dir=dev -l logging.conf --host=$(shell hostname -f)

# Release

LAST_COMMIT_MSG = $(shell git log -1 --pretty=%B | sed -e 's/\x27/"/g')
release: docker_trusty docs
	$(DOCKER_RUN) tron-builder-trusty /bin/bash -c " \
		dch -v $(VERSION) --distribution trusty --changelog debian/changelog \
			$$'$(VERSION) tagged with \'make release\'\rCommit: $(LAST_COMMIT_MSG)' && \
		chown $(UID):$(GID) debian/changelog \
"
	@git diff
	@echo "Now Run:"
	@echo 'git commit -a -m "Released $(VERSION) via make release"'
	@echo 'git tag --force v$(VERSION)'
	@echo 'git push --tags origin master'

# Docs

docs:
	tox -r -e docs

man:
	which $(SPHINXBUILD) >/dev/null && $(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(DOCS_DIR) $(DOCS_DIR)/man || true
	@echo
	@echo "Build finished. The manual pages are in $(DOCS_BUILDDIR)/man."

clean:
	rm -rf tronweb/js/cs
	find . -name '*.pyc' -delete
