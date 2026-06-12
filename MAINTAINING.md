Maintaining this fork
=====================

This is a fork of [`lh3/seqtk`](https://github.com/lh3/seqtk) with the
`telo -i` addition (see [NEWS.md](NEWS.md)). The local remotes are:

* `origin`   → `git@github.com:jbh-cas/seqtk.git`   (this fork — push here)
* `upstream` → `https://github.com/lh3/seqtk.git`   (Heng Li's; read-only)

Pull Heng Li's updates and push the merged result to the fork:

```sh
git pull upstream master
git push
```

That's it. `git pull` and `git push` on their own only know about `origin`
(your fork), so to fetch Heng Li's changes you have to name `upstream`
explicitly.
