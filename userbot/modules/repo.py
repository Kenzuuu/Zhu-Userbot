



@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """For .repo command, just returns the repo URL."""
    await wannasee.edit(
        f"**REPOSITORY**\n"
        f"💞 **[[[R̸E̸P̸O̸​](https://github.com/Kenzuuu/Zhu-Userbot)]]** 💞 **[[[O̸W̸N̸E̸R̸](t.me/triplenineee)]]** 💞\n"
    )
