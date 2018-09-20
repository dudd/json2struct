#!/usr/bin/python3
"""
Convert json string to golang struct.
"""

import os, json

space = "    "
fmt = "{0}{1:25s}{2:15s}`json:\"{3}\"`\n"
list_fmt = "{0}{1:25s}[]{2:13s}`json:\"{3}\"`\n"
structs = {}

def normallize(name) :
	return name.capitalize()

def conv_list(jlist, struct_name, key_name, old_key) :
	"""
	Convert list, we simply think that the element types in the list are the same.
	Don't handle two-dimensional or multidimensional list.
	If jlist is none, we consider it's a string list.
	"""
	global space, structs
	item = jlist[0] if jlist else "string"
	if isinstance(item, str) or isinstance(item, unicode):
		structs[struct_name] += list_fmt.format(space, key_name, "string", old_key)
	elif isinstance(item, bool) :
		structs[struct_name] += list_fmt.format(space, key_name, "bool", old_key)
	elif isinstance(item, int) :
		structs[struct_name] += list_fmt.format(space, key_name, "int64", old_key)
	elif isinstance(item, float) :
		structs[struct_name] += list_fmt.format(space, key_name, "float64", old_key)
	elif isinstance(item, list) :
		pass
	elif isinstance(item, dict) :
		structs[struct_name] += list_fmt.format(space, key_name, key_name, old_key)
		conv(item, key_name)
	else :
		pass

def conv(jsonstr, struct_name) :

	global structs, fmt, space
	if struct_name in structs.keys() : return
	structs[struct_name] = "type %s struct {\n" % struct_name

	for k, v in jsonstr.items() :
		new_k = "".join(list(map(normallize, k.split('_'))))
		if isinstance(v, str) or isinstance(v, unicode) :
			structs[struct_name] += fmt.format(space, new_k, "string", k)
		elif isinstance(v, bool) :
			structs[struct_name] += fmt.format(space, new_k, "bool", k)
		elif isinstance(v, int) :
			structs[struct_name] += fmt.format(space, new_k, "int64", k)
		elif isinstance(v, float) :
			structs[struct_name] += fmt.format(space, new_k, "float64", k)
		elif isinstance(v, list) :
			conv_list(v, struct_name, new_k, k)
		elif isinstance(v, dict) :
			structs[struct_name] += fmt.format(space, new_k, new_k, k)
			conv(v, new_k)
		else :
			pass

	structs[struct_name] += "}"


if __name__ == "__main__" :
	global status
	s = """
{
  "total_count": 2,
  "incomplete_results": false,
  "items": [
    {
      "url": "https://api.github.com/repos/dudd/github-issues-tools/issues/2",
      "repository_url": "https://api.github.com/repos/dudd/github-issues-tools",
      "labels_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/2/labels{/name}",
      "comments_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/2/comments",
      "events_url": "https://api.github.com/repos/dudd/github-issues-tools/issues/2/events",
      "html_url": "https://github.com/dudd/github-issues-tools/issues/2",
      "id": 362009608,
      "node_id": "MDU6SXNzdWUzNjIwMDk2MDg=",
      "number": 2,
      "title": "test",
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
      "state": "closed",
      "locked": false,
      "assignee": null,
      "assignees": [

      ],
      "milestone": null,
      "comments": 0,
      "created_at": "2018-09-20T03:58:08Z",
      "updated_at": "2018-09-20T03:59:08Z",
      "closed_at": "2018-09-20T03:59:08Z",
      "author_association": "OWNER",
      "body": "test111",
      "score": 1.0
    },
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
	while isinstance(j, list):
		j = j[0]
	conv(j, "DDD")

	for k, v in structs.items() :
		print("{}\n".format(v))
