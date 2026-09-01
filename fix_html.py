import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The cards look like this:
# <a class="project-card" ...>
#   <div class="media ratio-4-3">...</div>
#   <div class="body">...</div>
# </div>

# Let's fix the closing </div> to </a> where the opening tag is <a class="project-card"
def fix_closing(match):
    # match.group(0) is the whole card from <a class="project-card"... to the wrong </div>
    return match.group(0)[:-6] + '</a>' # replace last </div> with </a>

# The regex matches <a class="project-card" ... followed by 2 divs, then the closing </div>
pattern = r'<a class="project-card".*?class="media ratio-4-3".*?</div>\s*<div class="body">.*?</div>\s*</div>'

content = re.sub(pattern, fix_closing, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed unclosed anchor tags in index.html")
