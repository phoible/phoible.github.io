source 'https://rubygems.org'

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

gem 'github-pages', versions['github-pages']
gem 'redcarpet'
gem 'kramdown', '>= 2.3.1'
gem "nokogiri", ">= 1.18.4"
