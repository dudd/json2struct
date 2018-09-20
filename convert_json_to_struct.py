#!/usr/bin/python3
"""
Convert json string to golang struct.
"""

import os, json

level, space = (0, "    ")
fmt = "{0}{1}\t{2}\t`json:\"{3}\"`"
list_fmt = "{0}{1}\t[]{2}\t`json:\"{3}\"`"

def normallize(name) :
	return name.capitalize()

def conv_list(jlist, new_k, k) :
	"""
	Convert list, we simply think that the element types in the list are the same.
	Don't handle two-dimensional or multidimensional list.
	If jlist is none, we consider it's a string list.
	"""
	global space, level
	item = jlist[0] if jlist else "string"
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
		print("%s%s\t[]struct{" % (space * level, new_k))
		conv(item)
		print("%s}\t`json:\"%s\"`" % (space * level, k))
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
			print("%s%s\tstruct{" % (space * level, new_k))
			conv(v)
			print("%s}\t`json:\"%s\"`" % (space * level, k))
		else :
			pass

	if level == 1 :
		print("}")
	level -= 1


if __name__ == "__main__" :
	s = """
{
  "total_count": 1,
  "incomplete_results": false,
  "items": [
    {
      "url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1",
      "repository_url": "https://api.github.com/repos/dudd/github-issues-tools",
      "labels_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1/labels{/name}",
      "comments_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1/comments",
      "events_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/1/events",
      "html_url": "https://github.com/dudd/github-issues-tools/issues/1",
      "id": 362009510,
      "node_id": "MDU6SXNzdWUzNjIwMDk1MTA=",
      "number": 1,
      "title": "first",
      "user": {
        "login": "dudd",
        "id": 5847073,
        "node_id": "MDQ6VXNlcjU4NDcwNzM=",
        "avatar_url": "https://avatars0.githubusercontent.com/u/5847073?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dudd",
        "html_url": "https://github.com/dudd",
        "followers_url": "https://api.github.com/users/dudd/followers",
        "following_url": "https://api.github.com/users/dudd/following{/other_user}",
        "gists_url": "https://api.github.com/users/dudd/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dudd/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dudd/subscriptions",
        "organizations_url": "https://api.github.com/users/dudd/orgs",
        "repos_url": "https://api.github.com/users/dudd/repos",
        "events_url": "https://api.github.com/users/dudd/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dudd/received_events",
        "type": "User",
        "site_admin": false
      },
      "labels": [

      ],
      "state": "open",
      "locked": false,
      "assignee": null,
      "assignees": [

      ],
      "milestone": null,
      "comments": 0,
      "created_at": "2018-09-20T03:57:35Z",
      "updated_at": "2018-09-20T03:57:35Z",
      "closed_at": null,
      "author_association": "OWNER",
      "body": "test",
      "score": 1.0
    }
  ]
}
"""

	j = json.loads(s)
	conv(j)
