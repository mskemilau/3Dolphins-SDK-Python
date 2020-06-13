from collections import OrderedDict
import json


class ExtensionResult:
    def __init__(self, output, success=True, repeat=False, next_entity=True, agent=False):
        self.value = OrderedDict(output=output)
        self.success = success
        self.repeat = repeat
        self.next_entity = next_entity
        self.agent = agent

    def get_value(self):
        result = OrderedDict()
        result['value'] = self.value
        result['success'] = self.success
        result['repeat'] = self.repeat
        result['next'] = self.next_entity
        result['agent'] = self.agent
        return json.dumps(result)


class ExtensionRequest:
    def __init__(self, value):
        if 'intent' in value:
            self.intent = self.Intent(value['intent'])
        else:
            self.parameters = None
        if 'parameters' in value:
            self.parameters = value['parameters']
        else:
            self.parameters = None
        if 'commandName' in value:
            self.command_name = value['commandName']
        else:
            self.command_name = None
        if 'promptVariable' in value:
            self.prompt_variable = value['promptVariable']
        else:
            self.prompt_variable = None
        if 'integrationType' in value:
            self.integration_type = value['integrationType']
        else:
            self.integration_type = None

    def get_entity_value(self, val):
        for entity in self.parameters:
            if entity['name'] is val:
                return entity['value']
        return None

    class Intent:
        def __init__(self, value):
            if 'ticket' in value:
                self.ticket = self.Ticket(value['ticket'])
            else:
                self.ticket = None
            if 'intention' in value:
                self.intention = value['intention']
            else:
                self.intention = None
            if 'id' in value:
                self.id = value['id']
            else:
                self.id = None
            if 'botId' in value:
                self.botId = value['botId']
            else:
                self.botId = None
            if 'botToken' in value:
                self.botToken = value['botToken']
            else:
                self.botToken = None

        class Ticket:
            def __init__(self, value):
                if 'accessHash' in value:
                    self.accessHash = value['accessHash']
                else:
                    self.accessHash = None
                if 'accountId' in value:
                    self.accountId = value['accountId']
                else:
                    self.accountId = None
                if 'accountName' in value:
                    self.accountName = value['accountName']
                else:
                    self.accountName = None
                if 'accountScreen' in value:
                    self.accountScreen = value['accountScreen']
                else:
                    self.accountScreen = None
                if 'answer' in value:
                    self.answer = value['answer']
                else:
                    self.answer = None
                if 'appraised' in value:
                    self.appraised = value['appraised']
                else:
                    self.appraised = None
                if 'assignedAgent' in value:
                    self.assignedAgent = value['assignedAgent']
                else:
                    self.assignedAgent = None
                if 'assignedDate' in value:
                    self.assignedDate = value['assignedDate']
                else:
                    self.assignedDate = None
                if 'audioLink' in value:
                    self.audioLink = value['audioLink']
                else:
                    self.audioLink = None
                if 'availableAttachment' in value:
                    self.availableAttachment = value['availableAttachment']
                else:
                    self.availableAttachment = None
                if 'bigInfluencer' in value:
                    self.bigInfluencer = value['bigInfluencer']
                else:
                    self.bigInfluencer = None
                if 'channel' in value:
                    self.channel = value['channel']
                else:
                    self.channel = None
                if 'channelKey' in value:
                    self.channelKey = value['channelKey']
                else:
                    self.channelKey = None
                if 'channelType' in value:
                    self.channelType = value['channelType']
                else:
                    self.channelType = None
                if 'closedDate' in value:
                    self.closedDate = value['closedDate']
                else:
                    self.closedDate = None
                if 'closeInterval' in value:
                    self.closeInterval = value['closeInterval']
                else:
                    self.closeInterval = None
                if 'contactId' in value:
                    self.contactId = value['contactId']
                else:
                    self.contactId = None
                if 'correlationId' in value:
                    self.correlationId = value['correlationId']
                else:
                    self.correlationId = None
                if 'createdDate' in value:
                    self.createdDate = value['createdDate']
                else:
                    self.createdDate = None
                if 'createdDateStr' in value:
                    self.createdDateStr = value['createdDateStr']
                else:
                    self.createdDateStr = None
                if 'documentLink' in value:
                    self.documentLink = value['documentLink']
                else:
                    self.documentLink = None
                # Documents => List of String
                if 'documents' in value:
                    self.documents = value['documents']
                else:
                    self.documents = None
                if 'embedHtml' in value:
                    self.embedHtml = value['embedHtml']
                else:
                    self.embedHtml = None
                if 'errorCode' in value:
                    self.errorCode = value['errorCode']
                else:
                    self.errorCode = None
                if 'errorMessage' in value:
                    self.errorMessage = value['errorMessage']
                else:
                    self.errorMessage = None
                if 'errorShown' in value:
                    self.errorShown = value['errorShown']
                else:
                    self.errorShown = None
                if 'escalated' in value:
                    self.escalated = value['escalated']
                else:
                    self.escalated = None
                if 'escalatedDate' in value:
                    self.escalatedDate = value['escalatedDate']
                else:
                    self.escalatedDate = None
                if 'escalatedFrom' in value:
                    self.escalatedFrom = value['escalatedFrom']
                else:
                    self.escalatedFrom = None
                if 'escalatedTo' in value:
                    self.escalatedTo = value['escalatedTo']
                else:
                    self.escalatedTo = None
                if 'followerCount' in value:
                    self.followerCount = value['followerCount']
                else:
                    self.followerCount = None
                if 'friendCount' in value:
                    self.friendCount = value['friendCount']
                else:
                    self.friendCount = None
                if 'fromGroup' in value:
                    self.fromGroup = value['fromGroup']
                else:
                    self.fromGroup = None
                if 'id' in value:
                    self.id = value['id']
                else:
                    self.id = None
                if 'incoming' in value:
                    self.incoming = value['incoming']
                else:
                    self.incoming = None
                if 'latitude' in value:
                    self.latitude = value['latitude']
                else:
                    self.latitude = None
                if 'longitude' in value:
                    self.longitude = value['longitude']
                else:
                    self.longitude = None
                if 'mention' in value:
                    self.mention = value['mention']
                else:
                    self.mention = None
                if 'message' in value:
                    self.message = value['message']
                else:
                    self.message = None
                if 'messageId' in value:
                    self.messageId = value['messageId']
                else:
                    self.messageId = None
                if 'notified' in value:
                    self.notified = value['notified']
                else:
                    self.notified = None
                if 'openDate' in value:
                    self.openDate = value['openDate']
                else:
                    self.openDate = None
                if 'parent' in value:
                    self.parent = value['parent']
                else:
                    self.parent = None
                if 'pendingDate' in value:
                    self.pendingDate = value['pendingDate']
                else:
                    self.pendingDate = None
                if 'phone' in value:
                    self.phone = value['phone']
                else:
                    self.phone = None
                if 'pictureLink' in value:
                    self.pictureLink = value['pictureLink']
                else:
                    self.pictureLink = None
                if 'post' in value:
                    self.post = value['post']
                else:
                    self.post = None
                if 'profileLink' in value:
                    self.profileLink = value['profileLink']
                else:
                    self.profileLink = None
                if 'redistribute' in value:
                    self.redistribute = value['redistribute']
                else:
                    self.redistribute = None
                if 'remark' in value:
                    self.remark = value['remark']
                else:
                    self.remark = None
                if 'replyAgent' in value:
                    self.replyAgent = value['replyAgent']
                else:
                    self.replyAgent = None
                if 'replyCc' in value:
                    self.replyCc = value['replyCc']
                else:
                    self.replyCc = None
                if 'responseTime' in value:
                    self.responseTime = value['responseTime']
                else:
                    self.responseTime = None
                if 'responseTimeAgent' in value:
                    self.responseTimeAgent = value['responseTimeAgent']
                else:
                    self.responseTimeAgent = None
                if 'status' in value:
                    self.status = value['status']
                else:
                    self.status = None
                if 'subject' in value:
                    self.subject = value['subject']
                else:
                    self.subject = None
                if 'supervisor' in value:
                    self.supervisor = value['supervisor']
                else:
                    self.supervisor = None
                if 'ticketNumber' in value:
                    self.ticketNumber = value['ticketNumber']
                else:
                    self.ticketNumber = None
                if 'toGroup' in value:
                    self.toGroup = value['toGroup']
                else:
                    self.toGroup = None
                if 'transferDate' in value:
                    self.transferDate = value['transferDate']
                else:
                    self.transferDate = None
                if 'transfered' in value:
                    self.transfered = value['transfered']
                else:
                    self.transfered = None
                if 'transferedFrom' in value:
                    self.transferedFrom = value['transferedFrom']
                else:
                    self.transferedFrom = None
                if 'transferedTo' in value:
                    self.transferedTo = value['transferedTo']
                else:
                    self.transferedTo = None
                if 'version' in value:
                    self.version = value['version']
                else:
                    self.version = None
                if 'videoLink' in value:
                    self.videoLink = value['videoLink']
                else:
                    self.videoLink = None
                if 'ruleId' in value:
                    self.ruleId = value['ruleId']
                else:
                    self.ruleId = None
                if 'ruleOwner' in value:
                    self.ruleOwner = value['ruleOwner']
                else:
                    self.ruleOwner = None
                if 'ticketOwner' in value:
                    self.ticketOwner = value['ticketOwner']
                else:
                    self.ticketOwner = None
                if 'unassignedDate' in value:
                    self.unassignedDate = value['unassignedDate']
                else:
                    self.unassignedDate = None
                if 'unassignedDateText' in value:
                    self.unassignedDateText = value['unassignedDateText']
                else:
                    self.unassignedDateText = None
                if 'unassignedDuration' in value:
                    self.unassignedDuration = value['unassignedDuration']
                else:
                    self.unassignedDuration = None
                if 'greetingStatus' in value:
                    self.greetingStatus = value['greetingStatus']
                else:
                    self.greetingStatus = None
                # Documents => List of String
                if 'ticketTags' in value:
                    self.ticketTags = value['ticketTags']
                else:
                    self.ticketTags = None
                if 'clientMessageId' in value:
                    self.clientMessageId = value['clientMessageId']
                else:
                    self.clientMessageId = None
                if 'language' in value:
                    self.language = value['language']
                else:
                    self.language = None
                if 'userMessage' in value:
                    self.userMessage = value['userMessage']
                else:
                    self.userMessage = None
