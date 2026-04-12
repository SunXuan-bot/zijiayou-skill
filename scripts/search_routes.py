#!/usr/bin/env python3
"""路线库搜索工具"""
import json, sys, os

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(SKILL_DIR, 'data', 'routes_travel.json')

def load_routes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, encoding='utf-8') as f:
        return json.load(f)

def search_routes(routes, province=None, days=None, keyword='', limit=10):
    results = routes
    
    # 按省份过滤
    if province:
        results = [r for r in results if province in r.get('省份', '')]
    
    # 按天数过滤（±1天容差）
    if days:
        d = int(days)
        results = [r for r in results if abs(r.get('天数', 0) - d) <= 1]
    
    # 按关键词搜索
    if keyword:
        kw = keyword.lower()
        results = [r for r in results if 
            kw in r.get('线路名称', '').lower() or 
            kw in r.get('线路亮点', '').lower() or
            kw in r.get('省份', '').lower()]
    
    # 按天数排序
    results.sort(key=lambda r: r.get('天数', 0))
    
    return results[:limit]

def format_route(r):
    """格式化输出单条路线"""
    lines = [
        f"【{r['省份']}·{r['天数']}日】{r['线路名称'][:40]}",
        f"  亮点：{r.get('线路亮点', '')[:150]}...",
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    routes = load_routes()
    print(f'路线库共 {len(routes)} 条\n')
    
    # 无参数时输出全部省份统计
    if len(sys.argv) == 1:
        from collections import Counter
        provinces = Counter(r['省份'] for r in routes)
        print('各省份路线数：')
        for p, c in sorted(provinces.items(), key=lambda x: -x[1]):
            print(f'  {p}: {c}条')
        sys.exit(0)
    
    province = sys.argv[1] if len(sys.argv) > 1 else None
    days = sys.argv[2] if len(sys.argv) > 2 else None
    keyword = sys.argv[3] if len(sys.argv) > 3 else ''
    
    results = search_routes(routes, province, days, keyword)
    print(f'找到 {len(results)} 条结果：\n')
    for r in results:
        print(format_route(r))
        print()
