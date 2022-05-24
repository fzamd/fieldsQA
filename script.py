import itertools

CREATE_NEW_ATTR = [
	{
		'label': 'Fields',
		'values': ['All Type', 'None']
	},
	{
		'label': 'Parent Campaign',
		'values': ['With Fields (All Type)', 'Without Fields', 'None']
	},
	{
		'label': 'Workflow',
		'values': ['Rigid With Fields (All Type)', 'Rigid Without Fields', 'Flexible With Fields (All Type)', 'Flexible Without Fields', 'None']
	}
]

UPDATE_INIT_TASK_ATTR = [
	{
		'label': 'Init Workflow',
		'values': ['Rigid With Fields (All Type)', 'Rigid Without Fields', 'Flexible with Fields (All Type)', 'Flexible Without Fields', 'None']
	},
	{
		'label': 'Init Parent Campaign',
		'values': ['With Fields (All Type)', 'Without Fields', 'None']
	},
	{
		'label': 'Init Fields',
		'values': ['All Type', 'None']
	},
	{
		'label': 'Init Brief',
		'values': ['Template With Fields (All Type)', 'Template Without Fields (All Type)', 'None']
	}
]

TASK_VIEWS = {
	'Create': [
		{
			'label': 'Create New',
			'attributes': CREATE_NEW_ATTR,
			'sub_views': []
		},
		{
			'label': 'Notepad',
			'attributes': [
				{
					'label': 'Notes',
					'values': ['Random Note 1']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
		{
			'label': 'Task Details',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Source Task Fields',
					'values': ['All Type', 'None']
				},
				{
					'label': 'Source Task Has Workflow',
					'values': ['True', 'False']
				}
			],
			'sub_views': [
				{
					'label': 'Copy Task',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
		{
			'label': 'Campaign Details::Copy',
			'attributes': [],
			'sub_views': [
				{
					'label': 'Copy Campaign',
					'allow_attributes_permutation': False,
					'attributes': [
						{
							'label': 'Destination Parent Campaign',
							'values': ['With Fields', 'Without Fields', 'None']
						},
						{
							'label': 'Copy Task',
							'values': ['True', 'False']
						}
					]
				},
			]
		},
		{
			'label': 'Campaign Details::Tasks Tab',
			'attributes': [],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				},
			]
		},
		{
			'label': 'Library::Assets',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Content Type',
					'values': ['Article', 'Image']
				},
				{
					'label': 'Content Labels',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
		{
			'label': 'Library::Collections',
			'attributes': [
				{
					'label': 'Asset Labels',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
		{
			'label': 'Marketplace',
			'attributes': [
				{
					'label': 'Content',
					'values': ['Article', 'Image']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
		{
			'label': 'Request::Work Request',
			'attributes': [
				{
					'label': 'Work Request Fields',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
		{
			'label': 'Request::Pitch Request',
			'attributes': [
				{
					'label': 'Pitch Request Labels',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
		{
			'label': 'Plan::List',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['With Labels', 'Without Labels', 'None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Calendar',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Timeline',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['With Labels', 'Without Labels', 'None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Board',
			'attributes': [],
			'sub_views': [
				{
					'label': 'Create New',
					'attributes': CREATE_NEW_ATTR
				}
			]
		},
	],
	'Read': [],
	'Update': [
		{
			'label': 'Task Details',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_TASK_ATTR,
			'sub_views': [
				{
					'label': 'Edit Fields',
					'attributes': [
						{
							'label': 'Field',
							'values': ['Add Fields (All Type)', 'Add Field Values (All Type)', 'Remove Fields (All Type)', 'Remove Field Values (All Type)', 'Drag Fields']
						}
					]
				},
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				},
				{
					'label': 'Edit Workflow',
					'attributes': [
						{
							'label': 'Workflow',
							'values': ['Change to Rigid Workflow With Fields (All Type)', 'Change to Rigid Workflow Without Fields', 'Remove Workflow']
						}
					]
				},
				{
					'label': 'Edit Brief Template',
					'attributes': [
						{
							'label': 'Template Action',
							'values': ['Change to Template With Fields (All Type)', 'Change to Template Without Fields (All Type)', 'Remove Brief']
						}
					]
				}
			]
		},
		{
			'label': 'Plan::List',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_TASK_ATTR,
			'sub_views': [
				{
					'label': 'Edit Fields',
					'attributes': [
						{
							'label': 'Field',
							'values': ['Add Fields (All Type)', 'Add Field Values (All Type)', 'Remove Fields (All Type)', 'Remove Field Values (All Type)', 'Drag Fields']
						}
					]
				},
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				},
				{
					'label': 'Edit Workflow',
					'attributes': [
						{
							'label': 'Workflow',
							'values': ['Change to Rigid Workflow With Fields (All Type)', 'Change to Rigid Workflow Without Fields', 'Remove Workflow']
						}
					]
				}
			]
		},
		{
			'label': 'Plan::Timeline',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_TASK_ATTR,
			'sub_views': [
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				}
			]
		},
		{
			'label': 'Plan::Board',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_TASK_ATTR,
			'sub_views': [
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				},
				{
					'label': 'Edit Labels',
					'attributes': [
						{
							'label': 'Label',
							'values': ['Add Label Values (All Type)', 'Remove Field Values (All Type)']
						}
					]
				},
			]
		},
		{
			'label': 'Campaign Details::Tasks',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Init Fields',
					'values': ['All Type', 'None']
				},
				{
					'label': 'Init Workflow',
					'values': ['Rigid With Fields (All Type)', 'Rigid Without Fields', 'Flexible with Fields (All Type)', 'Flexible Without Fields', 'None']
				},
			],
			'sub_views': [
				{
					'label': 'Edit Labels',
					'attributes': [
						{
							'label': 'Edit Labels',
							'values': ['Add Label Values (All Type)', 'Remove Label Values (All Type)']
						}
					]
				}
			]
		},
	],
	'Delete': []
}

CREATE_NEW_EVENT_ATTR = [
	{
		'label': 'Fields',
		'values': ['All Type', 'None']
	},
	{
		'label': 'Parent Campaign',
		'values': ['With Fields (All Type)', 'Without Fields', 'None']
	}
]

UPDATE_INIT_EVENT_ATTR = [
	{
		'label': 'Init Parent Campaign',
		'values': ['With Fields (All Type)', 'Without Fields', 'None']
	},
	{
		'label': 'Init Fields',
		'values': ['All Type', 'None']
	}
]

EVENT_VIEWS = {
	'Create': [
		{
			'label': 'Create New',
			'attributes': CREATE_NEW_EVENT_ATTR,
			'sub_views': []
		},
		{
			'label': 'Notepad',
			'attributes': [
				{
					'label': 'Notes',
					'values': ['Random Note 1']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_EVENT_ATTR
				}
			]
		},
		{
			'label': 'Campaign Details::Copy',
			'attributes': [],
			'sub_views': [
				{
					'label': 'Copy Campaign',
					'allow_attributes_permutation': False,
					'attributes': [
						{
							'label': 'Destination Parent Campaign',
							'values': ['With Fields', 'Without Fields', 'None']
						},
						{
							'label': 'Copy Event',
							'values': ['True', 'False']
						}
					]
				},
			]
		},
		{
			'label': 'Campaign Details::Events Tab',
			'attributes': [],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_EVENT_ATTR
				},
			]
		},
		{
			'label': 'Request::Work Request',
			'attributes': [
				{
					'label': 'Work Request Fields',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_EVENT_ATTR
				}
			]
		},
		{
			'label': 'Request::Pitch Request',
			'attributes': [
				{
					'label': 'Pitch Request Labels',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_EVENT_ATTR
				}
			]
		},
		{
			'label': 'Plan::List',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['With Labels', 'Without Labels', 'None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Calendar',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Timeline',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['With Labels', 'Without Labels', 'None']
				}
			],
			'sub_views': []
		},
	],
	'Read': [],
	'Update': [
		{
			'label': 'Event Details',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_EVENT_ATTR,
			'sub_views': [
				{
					'label': 'Edit Fields',
					'attributes': [
						{
							'label': 'Field',
							'values': ['Add Fields (All Type)', 'Add Field Values (All Type)', 'Remove Fields (All Type)', 'Remove Field Values (All Type)', 'Drag Fields']
						}
					]
				},
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				},
			]
		},
		{
			'label': 'Plan::List',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_EVENT_ATTR,
			'sub_views': [
				{
					'label': 'Edit Fields',
					'attributes': [
						{
							'label': 'Field',
							'values': ['Add Fields (All Type)', 'Add Field Values (All Type)', 'Remove Fields (All Type)', 'Remove Field Values (All Type)', 'Drag Fields']
						}
					]
				},
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				}
			]
		},
		{
			'label': 'Plan::Timeline',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_EVENT_ATTR,
			'sub_views': [
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				}
			]
		},
		{
			'label': 'Campaign Details::Events',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Init Fields',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Events',
					'attributes': [
						{
							'label': 'Edit Fields',
							'values': ['Add Field (All Type)', 'Add Field Values (All Type)', 'Remove Field Values (All Type)']
						}
					]
				}
			]
		},
	],
	'Delete': []
}

CREATE_NEW_CAMPAIGN_ATTR = [
	{
		'label': 'Fields',
		'values': ['All Type', 'None']
	},
	{
		'label': 'Parent Campaign',
		'values': ['With Fields (All Type)', 'Without Fields', 'None']
	},
	{
		'label': 'Template',
		'values': ['With Fields (All Type)', 'Fields', 'None']
	}
]

UPDATE_INIT_CAMPAIGN_ATTR = [
	{
		'label': 'Init Parent Campaign',
		'values': ['With Fields (All Type)', 'Without Fields', 'None']
	},
	{
		'label': 'Init Fields',
		'values': ['All Type', 'None']
	}
]

CAMPAIGN_VIEWS = {
	'Create': [
		{
			'label': 'Create New',
			'attributes': CREATE_NEW_CAMPAIGN_ATTR,
			'sub_views': []
		},
		{
			'label': 'Notepad',
			'attributes': [
				{
					'label': 'Notes',
					'values': ['Random Note 1']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_CAMPAIGN_ATTR
				}
			]
		},
		{
			'label': 'Campaign Details::Copy',
			'attributes': [
				{
					'label': 'Source Parent Campaign Fields',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Copy Campaign',
					'allow_attributes_permutation': False,
					'attributes': [
						{
							'label': 'Destination Parent Campaign',
							'values': ['With Fields', 'Without Fields', 'None']
						},
						{
							'label': 'Copy Fields',
							'values': ['True', 'False']
						}
					]
				}
			]
		},
		{
			'label': 'Request::Work Request',
			'attributes': [
				{
					'label': 'Work Request Fields',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Create New',
					'allow_attributes_permutation': False,
					'attributes': CREATE_NEW_CAMPAIGN_ATTR
				}
			]
		},
		{
			'label': 'Plan::List',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['With Labels', 'Without Labels', 'None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Timeline',
			'attributes': [
				{
					'label': 'Parent Campaign',
					'values': ['With Labels', 'Without Labels', 'None']
				}
			],
			'sub_views': []
		},
	],
	'Read': [],
	'Update': [
		{
			'label': 'Plan::List',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_CAMPAIGN_ATTR,
			'sub_views': [
				{
					'label': 'Edit Fields',
					'attributes': [
						{
							'label': 'Field',
							'values': ['Add Fields (All Type)', 'Add Field Values (All Type)', 'Remove Fields (All Type)', 'Remove Field Values (All Type)', 'Drag Fields']
						}
					]
				},
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				}
			]
		},
		{
			'label': 'Plan::Timeline',
			'allow_attributes_permutation': False,
			'attributes': UPDATE_INIT_CAMPAIGN_ATTR,
			'sub_views': [
				{
					'label': 'Edit Parent Campaign',
					'attributes': [
						{
							'label': 'Campaign',
							'values': ['Change to Campaign With Fields (All Type)', 'Change to Campaign Without Fields', 'Remove Campaign']
						}
					]
				}
			]
		},
		{
			'label': 'Campaign Details',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Init Fields',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Fields',
					'attributes': [
						{
							'label': 'Edit Fields',
							'values': ['Add Field (All Type)', 'Add Field Values (All Type)', 'Remove Field Values (All Type)']
						}
					]
				}
			]
		},
	],
	'Delete': []
}

CREATE_NEW_FIELD_ATTR = [
	{
		'label': 'Name',
		'values': ['<Insert Name>']
	}
]

UPDATE_FIELD_ATTR = [
	{
		'label': 'Type',
		'values': [
			'Checkbox', #
			'Date',
			'Image',
			'Dropdown (Multi-Select)', 
			'Dropdown (Single)', #
			'Label (Multi-Select)',
			'Label (Single)',
			'Multiline Text',
			'Number',
			'Number (Currency)',
			'Number (Percent)',
			'Radio Button', #
			'Rich Text', 
			'Text',
			'Video'
		]
	}
]

CREATE_FIELD_SUB_VIEW = [
	{
		'label': 'Create New::Text',
		'attributes': []
	},
	{
		'label': 'Create New::Date',
		'attributes': []
	},
	{
		'label': 'Create New::Image',
		'attributes': []
	},
	{
		'label': 'Create New::Video',
		'attributes': []
	},
	{
		'label': 'Create New::Rich Text',
		'attributes': []
	},
	{
		'label': 'Create New::Text Area',
		'attributes': []
	},
	{
		'label': 'Create New::Dropdown',
		'allow_attributes_permutation': False,
		'attributes': [
			{
				'label': 'Is Multi-Select',
				'values': ['True', 'False']
			},
			{
				'label': 'Options',
				'values': ['<Insert Options>', 'None']
			}
		]
	},
	{
		'label': 'Create New::Checkbox',
		'allow_attributes_permutation': False,
		'attributes': [
			{
				'label': 'Options',
				'values': ['<Insert Options>', 'None']
			}
		]
	},
	{
		'label': 'Create New::Radio',
		'allow_attributes_permutation': False,
		'attributes': [
			{
				'label': 'Options',
				'values': ['<Insert Options>', 'None']
			}
		]
	},
	{
		'label': 'Create New::Label',
		'allow_attributes_permutation': False,
		'attributes': [
			{
				'label': 'Is Multi-Select',
				'values': ['True', 'False']
			},
			{
				'label': 'Options',
				'values': ['<Insert Options>', 'None']
			},
			{
				'label': 'Show in Filter',
				'values': ['All', 'None']
			}
		]
	},
	{
		'label': 'Create New::Number',
		'allow_attributes_permutation': False,
		'attributes': [
			{
				'label': 'Sub-Type',
				'values': ['Number', 'Currency', 'Percent']
			},
			{
				'label': 'Options',
				'values': ['<Insert Options>', 'None']
			},
			{
				'label': 'Decimal Place',
				'values': ['<Insert Value>', 'None']
			},
			{
				'label': 'Show 1000 Separator',
				'values': ['True', 'False']
			}
		]
	},
]

FIELD_VIEWS = {
	'Create': [
		{
			'allow_attributes_permutation': False,
			'label': 'Create New::Task',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Create New::Campaign',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Create New::Event',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Settings::Fields',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Settings::Workflow',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Settings::Template',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Campaign Details::Fields',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Task Details::Fields',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
		{
			'allow_attributes_permutation': False,
			'label': 'Event Details::Fields',
			'attributes': CREATE_NEW_FIELD_ATTR,
			'sub_views': CREATE_FIELD_SUB_VIEW
		},
	],
	'Read': [],
	'Update': [
		{
			'allow_attributes_permutation': False,
			'label': 'Settings::Fields',
			'attributes': UPDATE_FIELD_ATTR,
			'sub_views': [
				{
					'label': 'Edit',
					'allow_attributes_permutation': False,
					'attributes': [
						{
							'label': 'Name',
							'values': ['<Insert Name>']
						},
						{
							'label': 'Option',
							'values': ['Add Options', 'None']
						},
						{
							'label': 'Show in Filter',
							'values': ['All', 'None']
						},
						{
							'label': 'Active Status',
							'values': ['True', 'False']
						}
					]
				},
				{
					'label': 'Delete',
					'attributes': []
				}
			]
		},
	],
	'Delete': []
}

ASSET_VIEWS = {
	'Create': [
		{
			'label': 'Library::Assets',
			'attributes': [],
			'sub_views': [ 
				{
					'label': 'Upload',
					'attributes': [
						{
							'label': 'Asset Labels',
							'values': ['All Type', 'None']
						}
					]
				}
			]
		},
		{
			'label': 'Task Details::Content',
			'attributes': [
				{
					'label': 'Task Labels',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Text Editor',
					'attributes': [
						{
							'label': 'Asset Labels',
							'values': ['None']
						}
					]
				},
				{
					'label': 'Upload',
					'attributes': [
						{
							'label': 'Asset Labels',
							'values': ['None']
						}
					]
				},
				{
					'label': 'Library',
					'attributes': [
						{
							'label': 'Asset Labels',
							'values': ['All Type', 'None']
						}
					]
				}
			]
		},
		{
			'label': 'Campaign Details::Content',
			'attributes': [
				{
					'label': 'Campaign Labels',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': [
				{
					'label': 'Upload',
					'attributes': [
						{
							'label': 'Asset Labels',
							'values': ['All Type', 'None']
						}
					]
				},
				{
					'label': 'Library',
					'attributes': [
						{
							'label': 'Asset Labels',
							'values': ['All Type', 'None']
						}
					]
				}
			]
		}
	],
	'Read': [],
	'Update': [],
	'Delete': []
}

SAVED_VIEW_VIEWS = {
	'Create': [
		{
			'label': 'Plan::List',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Filters::Fields',
					'values': ['Label (Standard)', 'Label (Custom)', 'Checkbox', 'Dropdown', 'Radio', 'All Type', 'None']
				},
				{
					'label': 'Columns',
					'values': ['All Fields', 'None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Calendar',
			'attributes': [
				{
					'label': 'Filters::Fields',
					'values': ['Label (Standard)', 'Label (Custom)', 'Checkbox', 'Dropdown', 'Radio', 'All Type', 'None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Timeline',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Filters::Fields',
					'values': ['Label (Standard)', 'Label (Custom)', 'Checkbox', 'Dropdown', 'Radio', 'All Type', 'None']
				},
				{
					'label': 'Columns',
					'values': ['All Fields', 'None']
				}
			],
			'sub_views': []
		},
		{
			'label': 'Plan::Board',
			'attributes': [
				{
					'label': 'Filters::Fields',
					'values': ['Label (Standard)', 'Label (Custom)', 'Checkbox', 'Dropdown', 'Radio', 'All Type', 'None']
				}
			],
			'sub_views': []
		},
	],
	'Read': [],
	'Update': [],
	'Delete': []
}

WORK_REQUEST_VIEWS = {
	'Create': [
		{
			'label': 'Request::Work Request',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Template',
					'values': ['With Fields', 'Without Fields']
				}
			],
			'sub_views': []
		},
	],
	'Read': [],
	'Update': [],
	'Delete': []
}

ROUTING_RULE_VIEWS = {
	'Create': [
		{
			'label': 'Settings::Routing Rule',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Template',
					'values': ['With Fields', 'Without Fields', 'None']
				},
				{
					'label': 'Field',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': []
		},
	],
	'Read': [],
	'Update': [],
	'Delete': []
}

TEMPLATE_VIEWS = {
	'Create': [
		{
			'label': 'Settings::Template',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Template Fields',
					'values': ['All Other Types', 'None']
				}
			],
			'sub_views': []
		},
	],
	'Read': [],
	'Update': [],
	'Delete': []
}

WORKFLOW_VIEWS = {
	'Create': [
		{
			'label': 'Settings::Workflow',
			'allow_attributes_permutation': False,
			'attributes': [
				{
					'label': 'Workflow Steps',
					'values': ['Single Steps', 'Multiple Step', 'Single Sub-Step', 'Multiple Sub-Step']
				},
				{
					'label': 'Step Action',
					'values': ['With Edit Fields', 'Without Edit Fields', 'None']
				},
				{
					'label': 'Fields',
					'values': ['All Type', 'None']
				}
			],
			'sub_views': []
		},
	],
	'Read': [],
	'Update': [],
	'Delete': []
}

OBJECTS_ACTIONS = [
	# {
	# 	'type': 'Task',
	# 	'action': 'Create',
	# 	'views': TASK_VIEWS['Create']
	# },
	# {
	# 	'type': 'Task',
	# 	'action': 'Read',
	# 	'views': TASK_VIEWS['Read']
	# },
	# {
	# 	'type': 'Task',
	# 	'action': 'Update',
	# 	'views': TASK_VIEWS['Update']
	# },
	# {
	# 	'type': 'Task',
	# 	'action': 'Delete',
	# 	'views': TASK_VIEWS['Delete']
	# },
	# {
	# 	'type': 'Event',
	# 	'action': 'Create',
	# 	'views': EVENT_VIEWS['Create']
	# },
	# {
	# 	'type': 'Event',
	# 	'action': 'Read',
	# 	'views': EVENT_VIEWS['Read']
	# },
	# {
	# 	'type': 'Event',
	# 	'action': 'Update',
	# 	'views': EVENT_VIEWS['Update']
	# },
	# {
	# 	'type': 'Event',
	# 	'action': 'Delete',
	# 	'views': EVENT_VIEWS['Delete']
	# },
	# {
	# 	'type': 'Campaign',
	# 	'action': 'Create',
	# 	'views': CAMPAIGN_VIEWS['Create']
	# },
	# {
	# 	'type': 'Campaign',
	# 	'action': 'Read',
	# 	'views': CAMPAIGN_VIEWS['Read']
	# },
	# {
	# 	'type': 'Campaign',
	# 	'action': 'Update',
	# 	'views': CAMPAIGN_VIEWS['Update']
	# },
	# {
	# 	'type': 'Campaign',
	# 	'action': 'Delete',
	# 	'views': CAMPAIGN_VIEWS['Delete']
	# },
	{
		'type': 'Field',
		'action': 'Create',
		'views': FIELD_VIEWS['Create']
	},
	# {
	# 	'type': 'Field',
	# 	'action': 'Update',
	# 	'views': FIELD_VIEWS['Update']
	# },
	# {
	# 	'type': 'Asset',
	# 	'action': 'Create',
	# 	'views': ASSET_VIEWS['Create']
	# },
	# {
	# 	'type': 'Saved View',
	# 	'action': 'Create',
	# 	'views': SAVED_VIEW_VIEWS['Create']
	# },
	# {
	# 	'type': 'Work Request',
	# 	'action': 'Create',
	# 	'views': WORK_REQUEST_VIEWS['Create']
	# },
	# {
	# 	'type': 'Routing Rule',
	# 	'action': 'Create',
	# 	'views': ROUTING_RULE_VIEWS['Create']
	# },
	# {
	# 	'type': 'Workflow',
	# 	'action': 'Create',
	# 	'views': WORKFLOW_VIEWS['Create']
	# },
]

def expand_permutation(perm):
	expanded_permutation = []
	for item in perm:
		iter_grp = []
		for value in item['values']:
			iter_grp.append({'label': item['label'], 'value': value})

		expanded_permutation.append(iter_grp)

	return expanded_permutation


def render_test_string(object, view, sub_view, test_iteration):
	test_origin_string = 'When ' + object['action'] + ' ' + object['type'] + ' from ' + view['label']
	sub_view_string = ''
	if sub_view:
		sub_view_string = '->' + sub_view['label']

	test_string = test_origin_string + sub_view_string + ', select'
	for selector in test_iteration:
		if 'select' == test_string[-6:]:
			test_string += ' ' + selector['label'] + '::' + selector['value']
		else:
			test_string += ', and ' + selector['label'] + '::' + selector['value']
	print('    ' + test_string)


def get_combinations(attributes, allow_permutations=True):
	if allow_permutations:
		return itertools.permutations(attributes);
		
	else:
		return [tuple(attributes)]


total_object_count = 0
for object in OBJECTS_ACTIONS:
	print(object['action'] + '::' + object['type'] + ':')
	for view in object['views']:
		test_view_count = 0
		print('  ' + view['label'] + ':')
		view_attribute_perms = get_combinations(view['attributes'], view.get('allow_attributes_permutation', True))
		for view_attribute_perm in view_attribute_perms:
			expanded_view_perm = expand_permutation(view_attribute_perm)
			if len(view['sub_views']):
				for sub_view in view['sub_views']:
					sub_view_attribute_perms = get_combinations(sub_view['attributes'], sub_view.get('allow_attributes_permutation', True))
					for sub_view_attribute_perm in sub_view_attribute_perms:
						expanded_sub_view_perm = expand_permutation(sub_view_attribute_perm)
						for test_iteration in itertools.product(*[*expanded_view_perm, *expanded_sub_view_perm]):
							test_view_count += 1
							render_test_string(object, view, sub_view, test_iteration)

			else:
				for test_iteration in itertools.product(*expanded_view_perm):
					test_view_count +=1
					render_test_string(object, view, None, test_iteration)

		total_object_count += test_view_count
		print ('  Total ' + view['label'] + ' tests: ', test_view_count)
		print ()
print ('Total ' + object['action'] + ': ', total_object_count)
print ()

