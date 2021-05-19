#Swift Processor

Process incoming raw SWIFT messages, convert them JSON and index them.

The implementation use case handles the processing of corporate actions.

| Type | Description | Reference |
|------|-------------|-----------|
|MT 564 | Corporate Action Notification | [ISO 15022](https://www.iso20022.org/15022/uhb/finmt564.htm)
|MT 565 | Corporate Action Instruction | [ISO 15022](https://www.iso20022.org/15022/uhb/finmt565.htm)
|MT 566 | Corporate Action Confirmation | [ISO 15022](https://www.iso20022.org/15022/uhb/finmt566.htm)
|MT 567 | Corporate Action Status and Processing Advice | [ISO 15022](https://www.iso20022.org/15022/uhb/finmt567.htm)
|MT 568 | Corporate Action Narrative | [ISO 15022](https://www.iso20022.org/15022/uhb/finmt568.htm)


###3rd Party Swift References
* https://my.euroclear.com/drm/DRM_HTML_Mega/SWIFT/Settlement/PAGES/367169935047EAEB.HTM
* https://www.waterstechnology.com/data-management/7632671/transforming-and-optimizing-corporate-actions-processing

###Reference implementations and projects

* https://github.com/roskakori/swiftmess
* https://github.com/danielquinn/mt103
* https://github.com/kadnan/PyMTMessages

###Useful reference info

* https://www.sepaforcorporates.com/swift-for-corporates/read-swift-message-structure/
* https://www.paiementor.com/swift-mt-message-block-2-application-header-description/





 