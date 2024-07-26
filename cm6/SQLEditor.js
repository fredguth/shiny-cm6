import cm6  from "./cm6.bundle.min.js";

if (Shiny) {
  class SQLEditorOutputBinding extends Shiny.OutputBinding {

    find(scope) {
      return scope.find(".shiny-sql-editor");
    }

    renderValue(el, payload) {      
      view = cm6.createEditorView(undefined, el);
      state = cm6.createEditorState(payload);
      view.setState(state);

    }
  }
  Shiny.outputBindings.register(
    new SQLEditorOutputBinding(),
    "shiny-sql-editor"
  );
}
