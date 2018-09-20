#!/usr/bin/python3
"""
Convert json string to golang struct.
"""

import os, json

level = 0
space = "    "
fmt = "{0}{1}\t{2}\t`json:\"{3}\"`"
list_fmt = "{0}{1}\t[]{2}\t`json:\"{3}\"`"

def normallize(name) :
	return name.capitalize()

def conv_list(jlist, new_k, k) :
"""
	convert list, don't handle two-dimensional or multidimensional list.
"""
	global space, level
	item = jlist[0]
	if isinstance(item, str) or isinstance(item, unicode):
		print(list_fmt.format(space * level, new_k, "string", k))
	elif isinstance(item, bool) :
		print(list_fmt.format(space * level, new_k, "bool", k))
	elif isinstance(item, int) :
		print(list_fmt.format(space * level, new_k, "int64", k))
	elif isinstance(item, float) :
		print(list_fmt.format(space * level, new_k, "float64", k))
	elif isinstance(item, list) :
		pass
	elif isinstance(item, dict) :
		print(list_fmt.format(space * level, new_k, "struct{", k))
		conv(item)
		print("%s}" % (space * level))
	else :
		pass

def conv(jsonstr) :

	global level, fmt, space
	level += 1
	if level == 1 :
		print("type XXX struct {")

	for k, v in jsonstr.items() :
		new_k = "".join(list(map(normallize, k.split('_'))))
		if isinstance(v, str) or isinstance(v, unicode) :
			print(fmt.format(space * level, new_k, "string", k))
		elif isinstance(v, bool) :
			print(fmt.format(space * level, new_k, "bool", k))
		elif isinstance(v, int) :
			print(fmt.format(space * level, new_k, "int64", k))
		elif isinstance(v, float) :
			print(fmt.format(space * level, new_k, "float64", k))
		elif isinstance(v, list) :
			conv_list(v, new_k, k)
		elif isinstance(v, dict) :
			print("%s%s\tstruct{\t\t`json:\"%s\"`" % (space * level, new_k, k))
			conv(v)
			print("%s}" % (space * level))
		else :
			pass

	if level == 1 :
		print("}")
	level -= 1


if __name__ == "__main__" :
	s = """
{
  "ddd" : {"test":{"haha":{"hehe":1}}},
  "sln1" : [1,2],
  "sln2" : ["123","234"],
  "sln3" : [true, false],
  "sln4" : [{"gege" : {"gaga":1}}],
  "url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1",
  "repository_url": "https://api.github.com/repos/dudd/github-issues-tools",
  "labels_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1/labels{/name}",
  "comments_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1/comments",
  "events_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1/events",
  "html_url": "https://github.com/dudd/github-issues-tools/issues/1",
  "id": 361655547,
  "node_id": "MDU6SXNzdWUzNjE2NTU1NDc=",
  "number": 1,
  "title": "test issue",
  "state": "open",
  "locked": false,
  "assignee": null,
  "milestone": null,
  "comments": 0,
  "created_at": "2018-09-19T09:21:51Z",
  "updated_at": "2018-09-19T09:21:51Z",
  "closed_at": null,
  "author_association": "OWNER",
  "body": "For test",
  "score": 1.0
}
"""

	j = json.loads(s)
	conv(j)
