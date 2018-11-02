Design Goals
In rough order of urgency and importance

* Express business logic with the right degree of abstraction from cross-functional concerns (asynchronous orchestration, service calling, logging, attribution, failure handling)
* Strict separation of functions,  data models and package dependencies:
	- Components depend on other components
	- Value classes compose into other value classes
* Extension points can be defined throughout legacy code, as needed
	- Code around the extension point need to be refactored, but not the whole application
* Components should assemble by the specific depending on the generic within layers. Arbitration / aggregation may expose a qualitatively different coherent interface to upper layers
* Composition of well-encapsulated components instead of inheritance to specialize behavior
* All the benefits which we require from federation (attribution, logging, failure handling) are core design goals which are also requirements for core components
	- As soon as a certain piece of code is expressed as a component, the cross-functional concerns are ensured whether it's owned by ourselves or external teams
* There is no scope but the request scope. All safe code lives implicitly in a request scope.
	* Hence no spring or Guice (or at most a severely constrained version of it)
* Scalable -- many 100 components per request, owned by many 100 teams
	- Components centrally orchestrated
* Run-time versioning -- instead of build-time version lock-in, allow for run-time version arbitration between components
	- Move the versioning problem outside of your scope
* Soft-Sandboxing plus Monitoring plus Attribution instead of Hard Sandboxes
* Configuration through code, unsharpen the edges through soft sandboxing
* Distributed deployments -- implementation packages should be deployable independent of interfaces, other components
* Performant -- guaranteeing maximal performance by centralizing data and orchestration on one hub host
* Create a superset of many currently defined over-specific abstractions (CommandProvider, various Adapters, DAL abstractions like Mapper)