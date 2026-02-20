class Solution:
    def subdomainVisits(self, cpdomains):
        from collections import defaultdict
        
        count = defaultdict(int)
        
        for entry in cpdomains:
            c, domain = entry.split()
            c = int(c)
            parts = domain.split('.')
            
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                count[sub] += c
        
        return [str(v) + " " + k for k, v in count.items()]
