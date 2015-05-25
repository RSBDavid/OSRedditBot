class CommentManager:
    comments = set()

    def addComment(self, id):
        self.comments.add(id)

    def removeComment(self, id):
        self.comments.remove(id)

    def commentExists(self, id):
        return self.comments.__contains__(id)

    def get(self):
        return self.comments






