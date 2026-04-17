#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音标题生成器 - 标题分析和生成核心模块
"""

import os
import json
import re
import random
from datetime import datetime
from typing import List, Dict, Optional, Tuple
try:
    import jieba
    JIEBA_AVAILABLE = True
except ImportError:
    JIEBA_AVAILABLE = False
    # Simple fallback for word segmentation
    def simple_segment(text):
        # For Chinese text, return individual characters as words
        # This is a very basic fallback
        return list(text)

from collections import Counter, defaultdict

import os
import sys

class DouyinTitleGenerator:
    def __init__(self, examples_dir: str = None):
        if examples_dir is None:
            # Get the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.examples_dir = os.path.join(script_dir, "..", "examples")
        else:
            self.examples_dir = examples_dir
        
        # Ensure absolute path
        self.examples_dir = os.path.abspath(self.examples_dir)
        
        self.title_library = {}
        self.patterns = {
            'emotional_words': ['震惊', '绝了', '太', '超级', '必须', '千万', '绝对', '真的', '竟然', '居然'],
            'numbers': ['1', '2', '3', '5', '10', '100', '99%', '100%'],
            'emojis': ['🔥', '💰', '😱', '💥', '✨', '🎯', '💯', '🚀', '⚡', '🌟'],
            'question_words': ['为什么', '如何', '什么', '哪里', '谁'],
            'power_words': ['秘密', '技巧', '方法', '攻略', '指南', '教程', '经验', '分享']
        }
        self.load_title_library()
    
    def load_title_library(self):
        """加载标题库"""
        if not os.path.exists(self.examples_dir):
            os.makedirs(self.examples_dir)
            return
        
        # 加载所有JSON文件
        for filename in os.listdir(self.examples_dir):
            if filename.endswith('.json'):
                category = filename.replace('.json', '')
                filepath = os.path.join(self.examples_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        self.title_library[category] = json.load(f)
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
    
    def save_title_library(self, category: str, titles: List[str]):
        """保存标题到指定类别"""
        if category not in self.title_library:
            self.title_library[category] = []
        
        # 去重并添加新标题
        existing_titles = set(self.title_library[category])
        new_titles = [title for title in titles if title not in existing_titles]
        self.title_library[category].extend(new_titles)
        
        # 保存到文件
        filepath = os.path.join(self.examples_dir, f"{category}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.title_library[category], f, ensure_ascii=False, indent=2)
    
    def extract_titles_from_text(self, text: str) -> List[str]:
        """从用户输入文本中提取标题"""
        titles = []
        
        # 移除常见的前缀
        text = re.sub(r'^(这些标题太火了|收藏一下|爆款标题|热门标题|标题示例)[:：]?\s*', '', text)
        
        # 按行分割
        lines = text.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 移除行号（如 "1. ", "2. " 等）
            line = re.sub(r'^\d+\.\s*', '', line)
            line = re.sub(r'^[一二三四五六七八九十]+\s*[、.]\s*', '', line)
            
            # 移除引号
            line = line.strip('"\'')
            
            # 如果行看起来像标题（包含中文字符且长度合理）
            if re.search(r'[\u4e00-\u9fff]', line) and len(line) >= 5 and len(line) <= 100:
                titles.append(line)
        
        return titles
    
    def analyze_title_patterns(self, titles: List[str]) -> Dict:
        """分析标题模式"""
        if not titles:
            return {}
        
        analysis = {
            'length_stats': {'min': float('inf'), 'max': 0, 'avg': 0},
            'common_words': Counter(),
            'emotional_indicators': [],
            'number_usage': [],
            'emoji_usage': [],
            'question_usage': [],
            'structure_patterns': []
        }
        
        total_length = 0
        all_words = []
        
        for title in titles:
            # 长度统计
            length = len(title)
            analysis['length_stats']['min'] = min(analysis['length_stats']['min'], length)
            analysis['length_stats']['max'] = max(analysis['length_stats']['max'], length)
            total_length += length
            
            # 分词
            if JIEBA_AVAILABLE:
                words = list(jieba.cut(title))
            else:
                words = simple_segment(title)
            all_words.extend(words)
            
            # 情感词检测
            emotional_found = []
            for word in self.patterns['emotional_words']:
                if word in title:
                    emotional_found.append(word)
            if emotional_found:
                analysis['emotional_indicators'].extend(emotional_found)
            
            # 数字检测
            numbers_found = re.findall(r'\d+[%％]?', title)
            if numbers_found:
                analysis['number_usage'].extend(numbers_found)
            
            # 表情符号检测
            emojis_found = re.findall(r'[🔥💰😱💥✨🎯💯🚀⚡🌟❤️👍]', title)
            if emojis_found:
                analysis['emoji_usage'].extend(emojis_found)
            
            # 疑问词检测
            question_found = []
            for word in self.patterns['question_words']:
                if word in title:
                    question_found.append(word)
            if question_found:
                analysis['question_usage'].extend(question_found)
            
            # 结构模式分析
            if title.endswith('！') or title.endswith('!'):
                analysis['structure_patterns'].append('exclamation')
            elif title.endswith('？') or title.endswith('?'):
                analysis['structure_patterns'].append('question')
            elif '，' in title or ',' in title:
                analysis['structure_patterns'].append('comma_break')
        
        # 计算平均长度
        analysis['length_stats']['avg'] = total_length / len(titles) if titles else 0
        analysis['length_stats']['min'] = min(analysis['length_stats']['min'], analysis['length_stats']['avg'])
        
        # 统计高频词（排除停用词）
        stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个'}
        filtered_words = [word for word in all_words if len(word) > 1 and word not in stop_words]
        analysis['common_words'] = Counter(filtered_words).most_common(20)
        
        # 转换为列表格式
        analysis['emotional_indicators'] = list(set(analysis['emotional_indicators']))
        analysis['number_usage'] = list(set(analysis['number_usage']))
        analysis['emoji_usage'] = list(set(analysis['emoji_usage']))
        analysis['question_usage'] = list(set(analysis['question_usage']))
        analysis['structure_patterns'] = list(set(analysis['structure_patterns']))
        
        return analysis
    
    def generate_titles(self, topic: str = "", category: str = "general", count: int = 5) -> List[str]:
        """生成新标题"""
        # 获取相关类别的标题进行模式分析
        relevant_titles = []
        if category in self.title_library:
            relevant_titles = self.title_library[category]
        elif self.title_library:
            # 如果没有指定类别，使用所有标题
            for titles in self.title_library.values():
                relevant_titles.extend(titles)
        
        if not relevant_titles:
            # 如果没有学习数据，使用默认模板
            return self._generate_default_titles(topic, count)
        
        # 分析模式
        patterns = self.analyze_title_patterns(relevant_titles)
        
        generated_titles = []
        for _ in range(count):
            title = self._create_title_from_patterns(topic, patterns)
            if title and title not in generated_titles:
                generated_titles.append(title)
        
        # 如果生成不够，补充默认模板
        while len(generated_titles) < count:
            default_title = self._generate_default_titles(topic, 1)[0]
            if default_title not in generated_titles:
                generated_titles.append(default_title)
            else:
                break
        
        return generated_titles[:count]
    
    def _create_title_from_patterns(self, topic: str, patterns: Dict) -> str:
        """基于模式创建标题"""
        if not patterns:
            return ""
        
        # 随机选择标题结构
        structures = [
            "{emotional}{topic}{number}{power}{emoji}",
            "{number}个{power}让你{topic}{emoji}",
            "千万不要{topic}！{emotional}{reason}{emoji}",
            "{topic}的秘密，就藏在这{number}个字里{emoji}",
            "为什么{topic}？{emotional}真相{emoji}",
            "{emotional}！{topic}的{power}大公开{emoji}"
        ]
        
        structure = random.choice(structures)
        
        # 准备替换值
        replacements = {
            'topic': topic or "这个",
            'emotional': random.choice(patterns['emotional_indicators']) if patterns['emotional_indicators'] else random.choice(self.patterns['emotional_words']),
            'number': random.choice(patterns['number_usage']) if patterns['number_usage'] else random.choice(['3', '5', '10']),
            'power': random.choice(patterns['common_words'])[0] if patterns['common_words'] else random.choice(self.patterns['power_words']),
            'emoji': random.choice(patterns['emoji_usage']) if patterns['emoji_usage'] else random.choice(self.patterns['emojis']),
            'reason': "原因竟然是这样" if random.random() > 0.5 else "99%的人都不知道"
        }
        
        # 构建标题
        title = structure.format(**replacements)
        
        # 清理多余的空格和标点
        title = re.sub(r'\s+', ' ', title).strip()
        title = re.sub(r'[，,]{2,}', '，', title)
        
        # 确保标题长度合理
        if len(title) < 8:
            title += f" {random.choice(self.patterns['power_words'])}{random.choice(self.patterns['emojis'])}"
        elif len(title) > 60:
            title = title[:60] + "..."
        
        return title
    
    def _generate_default_titles(self, topic: str, count: int) -> List[str]:
        """生成默认标题模板"""
        templates = [
            f"{topic}的3个绝招，让你的效果翻倍🔥",
            f"千万不要这样做！关于{topic}的99%人都踩过的坑😱",
            f"月入5W的秘密，就藏在{topic}这3个字里💰",
            f"为什么{topic}这么火？真相让人震惊💥",
            f"超级实用！{topic}的完整攻略，建议收藏✨",
            f"{topic}这样做，效果立竿见影💯",
            f"新手必看！{topic}的5个关键技巧🚀",
            f"绝了！{topic}竟然还能这样玩⚡"
        ]
        
        # 随机选择
        selected = random.sample(templates, min(count, len(templates)))
        return selected
    
    def get_library_summary(self) -> Dict:
        """获取标题库摘要"""
        summary = {}
        for category, titles in self.title_library.items():
            summary[category] = {
                'count': len(titles),
                'sample': titles[:3] if titles else []
            }
        return summary

def main():
    """命令行接口"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python title_generator.py <command> [args]")
        print("Commands: add, generate, list, analyze")
        return
    
    command = sys.argv[1]
    generator = DouyinTitleGenerator()
    
    if command == "add":
        if len(sys.argv) < 4:
            print("Usage: add <category> <titles...>")
            return
        category = sys.argv[2]
        titles = sys.argv[3:]
        generator.save_title_library(category, titles)
        print(f"Added {len(titles)} titles to category '{category}'")
    
    elif command == "generate":
        topic = sys.argv[2] if len(sys.argv) > 2 else ""
        category = sys.argv[3] if len(sys.argv) > 3 else "general"
        count = int(sys.argv[4]) if len(sys.argv) > 4 else 5
        titles = generator.generate_titles(topic, category, count)
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}")
    
    elif command == "list":
        summary = generator.get_library_summary()
        for category, info in summary.items():
            print(f"\n{category} ({info['count']} titles):")
            for title in info['sample']:
                print(f"  - {title}")
    
    elif command == "analyze":
        if len(sys.argv) < 3:
            print("Usage: analyze <category>")
            return
        category = sys.argv[2]
        if category in generator.title_library:
            patterns = generator.analyze_title_patterns(generator.title_library[category])
            print(json.dumps(patterns, ensure_ascii=False, indent=2))
        else:
            print(f"Category '{category}' not found")

if __name__ == "__main__":
    main()