# Simplify Path


# Description:
    # Given a string path, which is an absolute path (starting with a slash '/') to a file or 
    # directory in a Unix-style file system, convert it to the simplified canonical path.

    # In a Unix-style file system, a period '.' refers to the current directory, a double period '..' 
    # refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. 
    # For this problem, any other format of periods such as '...' are treated as file/directory names.

    # The canonical path should have the following format:

    # The path starts with a single slash '/'.
    # Any two directories are separated by a single slash '/'.
    # The path does not end with a trailing '/'.
    # The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
    # Return the simplified canonical path.


# Constraints
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.


# Result:
# Runtime: 28 ms, faster than 90.93% of Python3 online submissions for Simplify Path.
# Memory Usage: 14.3 MB, less than 46.75% of Python3 online submissions for Simplify Path.

# Solution


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Disects the path every '/'
        pathArray = path.split('/')

        # stack to hold each path directory
        s= []
        
        for p in pathArray:
            if p == '':
                continue
            elif p == '.':
                continue
            elif p == '..':
                if len(s) > 0:
                    s.pop()
                else:
                    continue
            else:
                s.append(p)
                
        
        simplifiedPath = ''
        
        # check if there's any
        if len(s) == 0:
            simplifiedPath = '/'
        else:
        # combines all path
            for path in s:
                simplifiedPath += '/' + path
                
        return simplifiedPath