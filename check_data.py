import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('data/latest.json', encoding='utf-8'))

moutai = [s for s in data['stocks'] if s['code'] == '600519']
print(f'贵州茅台记录数: {len(moutai)}')
for s in moutai:
    print(f"  {s['strategy']}: 分数={s['score']}, 七层评分={len(s.get('layer_scores', []))}维度")
    if s.get('raw_response'):
        print(f"  报告长度: {len(s['raw_response'])}字")
        # 检查是否包含一万元操作建议
        if '一万元' in s['raw_response']:
            print("  ✓ 包含一万元操作建议")
        else:
            print("  ✗ 不包含一万元操作建议")
