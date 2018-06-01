# A website domain like "discuss.leetcode.com" consists of various subdomains.
# At the top level, we have "com", at the next level, we have "leetcode.com",
# and at the lowest level, "discuss.leetcode.com". When we visit a domain like
# "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
#
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received),
# followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.
# leetcode.com".
#
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains,
# (in the same format as the input, and in any order), that explicitly counts the number of visits to
# each subdomain.



class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        d = dict()
        for i in cpdomains:
            cnt, full_domain = i.split()
            separate_domain = full_domain.split('.')
            for i in range(len(separate_domain)):
                domain = '.'.join(separate_domain[i:])
                if domain not in d:
                    d[domain] = int(cnt)
                else:
                    d[domain] += int(cnt)

        l = []
        for key in d:
            l.append(str(d[key]) + ' ' + str(key))

        return l