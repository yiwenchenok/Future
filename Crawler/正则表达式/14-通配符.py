

import re
"""
.*?   可有可无  不包括\n
.*+   至少有一个
[\s\S]* 可有可无 包括\n
"""
html = """
        <div class="lesson-list-middle">
            <p><span>课程名称 :<em class="ems">手绘场景进阶5期</em></span></p>
            <p><span>课次名称 :<em class="ems">手绘场景场景贴图3</em></span></p>
            <p>
                <span>授课教师 :<em class="ems">小刘</em></span>
                <span>时长 :<em class="ems">120 分钟 </em></span>
                <span>课程类型 :<em class="ems">直播课</em></span>
            </p>
        </div>

"""

result = re.findall('<div [\s\S]*<span>授课教师 :<em class="ems">(.*?)</em></span>[\s\S]*</div>',html)
print(result) #['小刘']